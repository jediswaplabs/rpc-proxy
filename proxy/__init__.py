from flask import Flask, request
from requests import post
import os


SITE_URL = os.environ.get('SITE_URL', None)
if not SITE_URL:
    raise Exception("'SITE_URL' env variable not specified")

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

app = Flask(__name__)


@app.route('/', methods=HTTP_METHODS)
def proxy():
    return post(SITE_URL, data=request.data).content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
