from flask import Flask, render_template, request, session,redirect,url_for
import mysql.connector


conn = mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="quanlynhanvien")
cursor = conn.cursor()
app = Flask(__name__)
app.secret_key = "supper secret key"



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM taikhoan WHERE username=%s AND password=%s',(username,password))
        record = cursor.fetchone()
        if record:
            session['logedin'] = True
            session['username'] = record[0]
            return redirect(url_for('customer'))
        else:
            msg='Sai tài khoản hoặc mật khẩu. vui lòng thử lại'
            return render_template('index.html')

@app.route("/customer")
def home():
    return render_template('customer.html',username=session['username'])

@app.route("/logout")
def logout():
    session.pop('logedin',None)
    session.pop('username', None)
    return url_for('login')

cursor.close()
conn.close()