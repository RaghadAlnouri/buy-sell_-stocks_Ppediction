import base64
import os
import json
import pandas as pd
import logging
from model import Log_Reg
from flask import Flask, request
from scr.predict import predict
log = logging.getLogger()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return f'Hello, enter ticker name to get prediction "/get_stock_val/<ticker>"!\n'


@app.route("/get_stock_val/<ticker>", methods=["GET"])
def get_stock_pred(ticker: str) -> str:
    prediction = predict(ticker)
    return f'{prediction}'

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
 