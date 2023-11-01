#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template, request
from flask_babel import Babel, get_locale

app = Flask(__name__)
babel = Babel(app)

def get_locale():
  """ get locale language """
  user_languages = request.accept_languages
  supported_languages = ['en', 'fr']
  return user_languages.best_match(supported_languages, default='en')


babel.init_app(app, locale_selector=get_locale)

@app.route('/', methods=['GET'])
def index():
  """ GET /
  Return:
    - 2-index.html
  """
  return render_template('2-index.html')


if __name__ == "__main__":
  app.run()
