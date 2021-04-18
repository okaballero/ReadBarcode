# -*- encoding: utf-8 -*-
from flask import Flask, request, jsonify
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS

import Controllers.documentController as docs

app = Flask(__name__)

CORS(app, resources=r'*')
app.config["DEBUG"] = True


@app.route('/')
def index():
    res = {
            "App_name": "Barcode Recognition",
            "u'Description": "Platform Bnext barcodeRecognition",
            "Version": "0.0.1"
         }
    return  jsonify(res)

@app.route('/documents', methods=['POST'])
def initSection():
    ctrl = docs.DocumentsController()
    res = ctrl.receiveFile(request)
    return  jsonify(res)

@app.route('/imageConvert', methods=['GET'])
def imageTransacction():
    ctrl = docs.DocumentsController()
    res = ctrl.convertImage()
    return  jsonify(res)

if __name__ == '__main__':
    app.run('0.0.0.0',port=8085)
