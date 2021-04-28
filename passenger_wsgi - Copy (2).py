import os
import sys

from flask import Flask, request, render_template, redirect, url_for

from flaskapp.main import app as application

project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, '/templates')
static_path = os.path.join(project_root, '/static')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)
