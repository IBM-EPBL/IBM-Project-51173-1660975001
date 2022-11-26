import os


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import ibm_db

dsn_hostname = "2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "kvl02892"
dsn_pwd ="mLEEax4Ly59qV8zO"
dsn_driver = "{IBMDB2CLI}"
dsn_database ="bludb"
dsn_port = "32328"
dsn_protocol = "TCPIP"
dsn_security ="SSL"
dsn_cert="DigiCertGlobalRootCA.crt"

dsn = (   
    "DATABASE={0};"

    "HOSTNAME={1};"
    "PORT={2};"
    "SECURITY={3};"
    "SSLServerCertificate={4};"
    "UID={5};"
    "PWD={6};"   
    ).format( dsn_database ,dsn_hostname, dsn_port,dsn_security,dsn_cert ,dsn_uid, dsn_pwd)

try: 
    conn=ibm_db.connect(dsn,'','')
    print("Connected")
    
except:
    print("Not Connected")    


app = Flask(__name__)

app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)



@app.route("/",methods= ['POST','GET'] )
def register() :
    
    if request.method == 'POST':
        
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']

        sql = "SELECT * FROM USERS WHERE USERNAME =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            print("ALREADY A MEMBER") 
        else:
            print("kkkkkkkkkkk")
            insert_sql = "INSERT INTO USERS VALUES (?,?,?)"
            prep_stmt = ibm_db.prepare(conn,insert_sql)
            ibm_db.bind_param(prep_stmt, 1, username)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.execute(prep_stmt)
            return redirect(url_for('home'))  
                  
    return render_template("register.html")
"""


@app.route('/email', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = Message('Twilio SendGrid Test Email', recipients=['ashfaqevp2@gmail.com'])
        msg.body = 'This is a test email!'
        msg.html = '<p>This is a test email!</p>'
        mail.send(msg)
        return redirect(url_for('index'))
    return render_template('index.html')

"""



@app.route("/home" )
def home() :
    return render_template("home.html")    

@app.route("/login" )
def login() :
    return render_template("login.html") 

#@app.route("/register" )
#def register() :
#    return render_template("register.html") 

@app.route("/dashboard" )
def dashboard() :
    return render_template("dashboard.html")

@app.route("/cart" )
def cart() :
    return render_template("cart.html")

@app.route("/product" )
def product() :
    return render_template("product.html")   


if __name__ == "__main__":
    app.debug = True
    app.run()    

  