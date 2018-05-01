#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask.views import MethodView

from flask_mongoengine import MongoEngine


db = MongoEngine()


def create_app(config):
    app = Flask(__name__)
    # app.config.from_object(config)

    # app.debug = True

    # app.config['DEBUG'] = True
    # app.config['MONGODB_SETTINGS'] = {'DB': 'RestBlog'}
    # app.config['MONGODB_SETTINGS'] = {'DB': 'ShawnBlog'}
    # app.config['MONGODB_SETTINGS'] = {'DB': 'shawnblog'}
    app.config['MONGODB_SETTINGS'] = {
    'db': 'shawnblog',
    'host': 'mongodb://shawn:shawnshao@ds263089.mlab.com:63089/shawnblog'
	}

    app.config['SECRET_KEY'] = 'secret'
    app.config['DATA_BACKEND'] = 'mongodb'
    app.config['PROJECT_ID'] = 'shorten-url-1491815099304'
    # app.config['MONGO_URI'] = ''

    db.init_app(app)

    return app

