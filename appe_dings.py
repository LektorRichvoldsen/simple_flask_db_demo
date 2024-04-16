from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def hovedside() -> 'html':
    return render_template('entry.html',
                           the_title='Velkommen til hovedsiden!')


@app.route('/erik')
def erikkode():
    return "Hei på deg"

@app.route('/insert', methods=['POST'])
def insert_ting() -> None:
    """Mottar data fra form."""
    dbconfig = { 'host': '127.0.0.1',
                 'user': 'root',
                 'password': 'root',
                 'database': 'demo_db', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into test_ting 
              (ting, tang)
              values
              (%s, %s)"""
    cursor.execute(_SQL, (request.form['ting'], 
                   request.form['tang'],))
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('vise_resultater.html',
                           the_title='Vis fram!')


@app.route('/read')
def vise_ting() -> 'html':
    dbconfig = { 'host': '127.0.0.1',
                 'user': 'root',
                 'password': 'root',
                 'database': 'demo_db', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """select ting, tang from test_ting"""
    cursor.execute(_SQL)
    contents = cursor.fetchall()
    titles = ('Ting', 'Tang')
    return render_template('vise_resultater.html',
                            the_title='Ting og Tang',
                            the_row_titles=titles,
                            the_data=contents,)


app.run(debug=True)