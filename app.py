from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('loginpass.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Loginpass (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL
)
''')

connection.commit()

connection.close()

@app.route("/", methods=['GET', 'POST'])
def gfg():
    if request.method == "POST":
       con = sqlite3.connect('loginpass.db')
       cur = con.cursor()
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       cur.execute(f'INSERT INTO Loginpass (username, password) VALUES (?, ?);', (first_name, last_name))
       con.commit()
       con.close()
       print(first_name+" "+last_name)
       return "Your name is "+first_name + last_name
    return render_template('attempt.html')

if __name__=='__main__':
    app.run()
