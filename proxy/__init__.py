from flask import Flask, request
from requests import post
import os


SITE_URL = os.environ.get('SITE_URL', None)
if not SITE_URL:
    raise Exception("'SITE_URL' env variable not specified")

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
}

app = Flask(__name__)


@app.route('/api/', methods=HTTP_METHODS)
def proxy():
    return post(SITE_URL, json=request.json, headers=HEADERS).content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
