from flask import Flask

apps = Flask(__name__)


@apps.route('/')
def hello():
    return 'Hello, World!-apps'

