#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

def get_locale():
  """ get locale language """
  user_languages = request.accept_languages
  supported_languages = ['en', 'fr']

  # Force locale if specified in the URL parameter
  locale = request.args.get('locale')
  if locale in supported_languages:
    return locale

  # Otherwise, return the best match from the user's languages
  return user_languages.best_match(supported_languages, default='en')

@app.route('/', methods=['GET'])
def index():
  """ GET /
  Return:
    - 4-index.html
  """
  return render_template('4-index.html')


if __name__ == "__main__":
  app.run()
