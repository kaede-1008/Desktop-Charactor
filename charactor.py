#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "hogehogehogehoge"
    
if __name__ == "__main__":
    print('on hello')
    app.run(host="127.0.0.1", port=5000)