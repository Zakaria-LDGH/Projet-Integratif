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

#connect BD
def create_Connection():
    db_path = "sqlite.db"
    if not os.path.exists(db_path):
        print(f"Le fichier {db_path} n'existe pas")
        connection = None
    else:
        try:
            connection = sqlite3.connect(db_path)
            print("Connection to SQLite reussie")
        except sqlite3.Error as e:
            print(f"The error {e} occured")
    return connection

#execute sql
def execute_query(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result, cursor.description
    except Exception as e :
        print(f"The error {e} occured")

#sans retour
def execute_sans(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        res = True
    except sqlite3.OperationalError as op:
        print(f"SQL error {op} occured")
        print(query)
        res = False
    except sqlite3.Error as e:
        print(f"The error {e} occured")
        print(traceback.print_exc())
        res = False
    return res


#check e-mail
def checkEmail(emailPart,connection)->bool:   
    query=f'''
    SELECT 1
    FROM utilisateur
    WHERE emailpart = '{mailUser}'
    limit 1
    '''
    resQuery=execute_query(connection,query)
    try:
        resQuery[0][0][0]
    except IndexError: #soit exeist, soit null
        rest=False
    else:
        rest=True
    return rest

############################ Afficher Web ###################################

@app.route("/")
def index():
    return render_template('index.html')
