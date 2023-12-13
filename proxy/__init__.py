from flask import Flask, request
from requests import post
import os


SITE_ENV = os.environ.get('SITE_ENV', None)
API_KEY = os.environ.get('API_KEY', None)
if SITE_ENV == "testnet":
    SITE_URL = f'https://starknet-goerli.infura.io/v3/{API_KEY}'
elif SITE_ENV == "mainnet":
    SITE_URL = f'https://starknet-mainnet.infura.io/v3/{API_KEY}'

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
}

app = Flask(__name__)


@app.route('/', methods=HTTP_METHODS)
def proxy():
    return post(SITE_URL, json=request.json, headers=HEADERS).content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
