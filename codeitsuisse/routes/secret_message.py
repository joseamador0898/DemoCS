import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def evaluateSecretMessages():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    #inputValue = data.get("input");
    result = []
    for test_case in data:
        result.append(encrypt(test_case["n"], test_case["text"]))
    logging.info("My result :{}".format(result))
    return jsonify(result);

    def encrypt(n,text):
        



