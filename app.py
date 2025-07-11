from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123",
    database="login"
)
cursor = db.cursor()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        Name = request.form['Name']
        MObile = request.form['Mobile']
        Password = request.form['Password']
        cursor.execute("INSERT INTO users (Name, Mobile,Password) VALUES (%s, %s ,%s)", (Name, Mobile, Password ))
        db.commit()
        return redirect('/login')
    return render_template('form.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE name=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        msg = 'Login successful' if user else 'Invalid credentials'
    return render_template('login_page.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)

