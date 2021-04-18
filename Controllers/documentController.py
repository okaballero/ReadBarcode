# -*- encoding: utf-8 -*-
import Config.config as cnn
from datetime import date
import uuid
import requests
import json
import time
from pyzbar.pyzbar import decode

import os

import base64
import io

from PIL import Image


class DocumentsController():
    def __init__(self):
        self.str1 = "First Class"
    def receiveFile(self, request):

        form = request.json
        imgdata = base64.b64decode(form['image'])
        filename = 'tmp_image_barcode.png'
        
        with open(filename, 'wb') as f:
            f.write(imgdata)

        img = Image.open(filename)

        result = decode(img)

        for i in result:
            try:
                return {'status': 200, 'data': i.data.decode("utf-8") }
            except:
                return {'status': 401, 'data': 'No se pudo identificar el barcode' }

    def convertImage(self):
        filename = 'barcodeHotcakes.jpeg'
        with open(filename, "rb") as img_file:
            my_string = base64.b64encode(img_file.read())

        print(my_string)
