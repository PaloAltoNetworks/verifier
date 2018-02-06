#!/usr/bin/python

import requests, json
from flask import Flask, request
app = Flask(__name__)

FIELD_TO_VERIFY = "publisher"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    target = "http://%s/%s" % (request.headers['Host'], path)

    r = requests.get(target)
    if r.status_code != 200:
        return r.text, r.status_code

    response_json = r.json()

    if FIELD_TO_VERIFY in response_json:
        response_json[FIELD_TO_VERIFY] = response_json[FIELD_TO_VERIFY] + " (verified)"

    return json.dumps(response_json), r.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
