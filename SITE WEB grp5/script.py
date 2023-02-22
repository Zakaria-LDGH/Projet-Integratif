from datetime import datetime
import traceback
from flask import Flask
from flask import render_template, request
import sqlite3,os

from flask import session
from flask import redirect, url_for



##################### Fonction ##############################

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
