#!/usr/bin/env python3
"""
Basic Babel setup in a Flask application.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Configuration for Babel setup.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Render the index page with a "Hello, World" message.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()
