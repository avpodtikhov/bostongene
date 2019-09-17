from app import app, celery, mail
from flask import request, jsonify
from flask_mail import Message

import hashlib
import requests

@app.route('/submit', methods=['POST'])
def submit():
    params = request.form.to_dict()
    if 'url' not in params:
        return jsonify({'status' : 'No url'}), 400
    if 'email' in params:
        task = countMD5.apply_async(args=[params['email'], params['url']])
    else:
        task = countMD5.apply_async(args=[None, params['url']])
    return jsonify({'id' : task.id}), 200

@celery.task(bind=True)
def countMD5(self, email, url):
    try:
        self.update_state(state='RUNNING')
        m = hashlib.md5()
        r = requests.get(url)
        for data in r.iter_content(4196):
            m.update(data)
        md5 = m.hexdigest()
        if email != None:
            msg = Message('MD5 hash', sender = 'apodtikhov@gmail.com', recipients = [email])
            msg.body = 'MD5 hash of the file (url = ' + url + ') is ' + str(md5)
            mail.send(msg)
        return {'url' : url, 'md5' : md5}
    except:
        self.update_state(state='FAILURE')
        return

@app.route('/check', methods=['GET'])
def check():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return jsonify({'status' : 'Error: No id field provided'}), 404
    task = countMD5.AsyncResult(id)
    if task.state == 'PENDING':
        return jsonify({'state' : 'does not exist'}), 400
    elif task.state == 'SUCCESS':
        return jsonify({'md5': task.info['md5'], 'state' : 'done', 'url' : task.info['url']}), 200
    elif task.state == 'FAILURE':
        return jsonify({'state' : 'failure'}), 404
    else:
        return jsonify({'state' : 'running'}), 202