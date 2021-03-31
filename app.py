from flask import Flask, request, redirect, render_template, session, url_for
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = 'snnwmlsd'
db = MySQL(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Ada870407"
app.config["MYSQL_DB"] = "weblogin"

@app.route('/member/')
def member():
    return render_template("member.html", name = session["name"])

# TO BE SOLVED
@app.route('/error/')
def error():
    message = request.args.get("message")
    return render_template("error.html", message = message)

@app.route('/')
def web():
    return render_template('web.html')


@app.route('/signup', methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        if "username" in request.form:
            username = request.form["username"]
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM weblog WHERE username = %s", [username])
            # cur.execute("SELECT * FROM weblog WHERE username = %s", (username))
            info = cur.fetchone()
            print(info)
            if info is not None:                             
                message = "帳號已被註冊"
                return redirect(url_for("error", message = message))
            else:
                cur.execute("INSERT INTO weblogin.weblog(name, username, password)VALUES(%s, %s, %s)", (request.form["name"], username, request.form["password"]))
                db.connection.commit()
                return redirect("/")

    return render_template("web.html")


@app.route('/signin', methods = ["GET", "POST"])
def signin():
    if request.method == "POST":
        if "username" in request.form and "password" in request.form:
            username = request.form["username"]
            password = request.form["password"]
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM weblog WHERE username = %s AND password = %s", (username, password))
            account = cur.fetchone()
            if account: 
                session["name"] = account["name"]
                return redirect(url_for('member'))
            else: 
                message = "帳號或密碼輸入錯誤"
                return redirect(url_for('error', message = message))
    return redirect(url_for('web'))


@app.route("/signout")
def signout():
    session.pop("username", None)
    session.pop("password", None)
    return redirect(url_for("web"))
    
app.run(port = 3000)
