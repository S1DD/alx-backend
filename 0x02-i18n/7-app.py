#!/usr/bin/env python3
'''Task 6: user user locale
'''
from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

class Config:
    '''Config class'''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[int, None]:
    """
    Gets the user based on their id
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request()
def before_request() -> None:
    """
    Carries out tasks before each request resolution
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config('LANGUAGES'):
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone() -> str:
    '''
    Gets the timezone for a web page
    '''
    timezone = request.args.get('timezone', '')
    if not timezone in g.user:
        timezone = g.user['timezone']
    
    try:
        pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']    



@app.route('/')
def index() -> str:
    '''
    Returns a web page
    ''' 
    return render_template("7-index.html")

if __name__ == "__main__":
    app.run()