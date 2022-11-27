import os
from flask import Flask, render_template, request, redirect, url_for, flash,session
from flask_mail import Mail, Message
import ibm_db
import bcrypt

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


conn1=ibm_db.connect(dsn,'','')
sql11 = "SELECT * FROM USERS"
stmt11 = ibm_db.exec_immediate(conn1, sql11)
dictionary1 = ibm_db.fetch_assoc(stmt11)
products1 = []

while dictionary1 != False:
    product1={'name':dictionary1["USERNAME"],
               'price':dictionary1["PWD"]}
    products1.append(product1)           
    dictionary1 = ibm_db.fetch_assoc(stmt11)

print(products1) 




app = Flask(__name__)

app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)


prds = [
    {
        'name':'Jhon Players',
        'type': 'Slim Fit Shirt',
        'price' : '750',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20221117/5h3S/6375d6fcaeb269659c97f575/dennislingo-premium-attire-black-classic-slim-fit-shirt-with-patch-pocket.jpg'
    },

    {
        'name':'Peter England',
        'type': 'Slim Fit Shirt',
        'price' : '700',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20221121/XGZR/637b5531f997ddfdbd87764e/dennislingo-premium-attire-green-classic-full-sleeves-slim-fit-shirt.jpg'
    },

    {
        'name':'Red Hoodies',
        'type': 'Hoodies',
        'price' : '1049',
        'img' : 'https://www.redwolf.in/image/cache/catalog/mens-t-shirts/full-sleeves/spider-man-logo-full-sleeves-t-shirt-india-2-700x700.jpg'
    },

    {
        'name':'Million Club',
        'type': 'Hoodies',
        'price' : '520',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/h71/hcb/14969096110110/difference-of-opinion-yellow-hoodies-typographic-hoodie.jpg'
    },

    
    {
        'name':'HRX',
        'type': 'Yellor T-Shirt',
        'price' : '540',
        'img' : 'https://storage.googleapis.com/brained-uat/hrx/subcatImage/subcatImage-Vts_V97DtVrvhvSEIJwbQ-1662612896'
    },

    {
        'name':'Eyebogler',
        'type': 'Polo T-Shirt',
        'price' : '450',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20220901/HOL6/6310ee7aaeb269dbb361c4cd/eyebogler-green-polo-striped-polo-t-shirt.jpg'
    },

     {
        'name':'Goregone',
        'type': 'Silk Saree',
        'price' : '2500',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20220921/RHqq/632acc02f997dd1f8d104b2e/gorgone-grey-printed-floral-print-mysore-silk-saree.jpg'
    },


     {
        'name':'Goregone',
        'type': 'Silk Saree',
        'price' : '2500',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20220919/ayzk/632852e3aeb269dbb3934ee4/gorgone-red-printed-ethnic-print-mysore-silk-saree.jpg'
    },


     {
        'name':'Long Kurta',
        'type': 'T Tabrid',
        'price' : '1200',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20210404/uPDv/606a4fa47cdb8c1f14964fa9/t-tabard-blue-regular-kurtas-floral-print-long-kurta.jpg'
    },

     {
        'name':'Namaskar',
        'type': 'Long Kurta',
        'price' : '1400',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20211111/TEEy/618d497ff997ddf8f10255f7/namaskar-red-regular-kurtas-block-print-long-kurta-with-mandarin-collar.jpg'
    },

     {
        'name':'Clafoutis',
        'type': 'T-Shirts',
        'price' : '700',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20220121/tjjr/61ea8001aeb2695cdd26b614/clafoutis-black-crew-full-sleeves-turtleneck-t-shirt.jpg'
    },

     {
        'name':'Gespo',
        'type': 'T-Shirts',
        'price' : '390',
        'img' : 'https://assets.ajio.com/medias/sys_master/root/20220217/NLKI/620e5ccef997dd03e2d5f523/gespo-blue-crew-high-neck-slim-fit-t-shirt.jpg'
    }

    
] 





@app.route("/")
def indexs():
  return render_template('index.html')





@app.route("/product",methods= ['POST','GET']  )
def product() :
    name=request.args.get('item')
    print(name)
    name_s=name

    res = None
    for sub in prds:
        if sub['name'] == name_s:
            res = sub
            break
    
    price= str(res.get('price')) 
    imgs= str(res.get('img')) 
    types= str(res.get('type')) 
    qnty ="1"
    if 'username' in session :
        user=session['username']
    else :
        user='Guest'    

    print(str(res.get('price')))

    if request.method == 'POST':
                
        print("Uploading data")
        insert_sql = "INSERT INTO PURCHASE VALUES (?,?,?,?,?,?)"
        prep_stmt = ibm_db.prepare(conn,insert_sql)
        ibm_db.bind_param(prep_stmt, 1, user)
        ibm_db.bind_param(prep_stmt, 2, name)
        ibm_db.bind_param(prep_stmt, 3, types)
        ibm_db.bind_param(prep_stmt, 4, qnty)
        ibm_db.bind_param(prep_stmt, 5, price)
        ibm_db.bind_param(prep_stmt, 6, imgs)        
        ibm_db.execute(prep_stmt)
        
        flash('Add To Purchase') 
        return redirect(url_for('cart')) 
    
    return render_template("product.html",name=name,price=price,types=types,imgs=imgs)   







@app.route("/register",methods= ['POST','GET'] )
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
            session['loggedin']=True
            session['username']=username
            #session['username']=account['USERNAME']
            flash('You Logged In') 
            return redirect(url_for('home')) 
                             
    return render_template("register.html")




@app.route("/home" )
def home() :
    return render_template('home.html', prds=prds) 




@app.route("/login" ,methods= ['POST','GET'])
def login() :
    msg=''
    if request.method == 'POST':
        
        username=request.form['username']
        password=request.form['password']

        sql = "SELECT * FROM USERS WHERE USERNAME =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            session['loggedin']=True
            session['username']=account['USERNAME']
            
           
            print("LOGGED") 
            flash('You Logged In') 
            return redirect(url_for('home')) 
            flash('You Logged In') 
        else:
            print("not account") 
            flash('Username or Passwor is Incorrect') 
            return redirect(url_for('login'))  
    return render_template('login.html',name='Home') 








@app.route("/logout" )
def logout() :
    session.pop('loggedin',None)
    #session.pop('id',None)
    session.pop('username',None)
    return redirect(url_for('home')) 





@app.route("/account" )
def account() :

    if session.get('loggedin'):
         return redirect(url_for('profile'))   
    else :
         return redirect(url_for('login'))     

    return render_template("account.html")             



@app.route("/homes")
def dis():
  col3_list=[]

  return render_template('pro.html',col3=col3_list) 


  


@app.route("/profile" )
def profile() :
    return render_template("profile.html")  


@app.route("/admin" )
def admin() :

    conn=ibm_db.connect(dsn,'','')

    sql1 = "SELECT * FROM PURCHASE "
    stmt1 = ibm_db.exec_immediate(conn, sql1)
    dictionary = ibm_db.fetch_assoc(stmt1)
    carts = []

    while dictionary != False:
        product={'user':dictionary["USERS"],
                'name':dictionary["NAMES"],
                'type':dictionary["TYPES"],
                'qnty':dictionary["QNTS"],
                'img':dictionary["IMGS"],
                'price':dictionary["PRICES"]}
        carts.append(product)           
        dictionary = ibm_db.fetch_assoc(stmt1)

    return render_template("adminpage.html",carts=carts)            

 

@app.route("/dashboard" )
def dashboard() :
    return render_template("dashboard.html")


@app.route("/about" )
def about() :
    return render_template("about.html")




@app.route("/cart" )
def cart() :

   
    if 'username' in session :
        user=session['username']
    else :
        user='Guest'  


    conn=ibm_db.connect(dsn,'','')



    sql1 = "SELECT * FROM PURCHASE "
    stmt1 = ibm_db.exec_immediate(conn, sql1)
    dictionary = ibm_db.fetch_assoc(stmt1)
    carts = []

    while dictionary != False:
        product={'user':dictionary["USERS"],
                'name':dictionary["NAMES"],
                'type':dictionary["TYPES"],
                'qnty':dictionary["QNTS"],
                'img':dictionary["IMGS"],
                'price':dictionary["PRICES"]}
        carts.append(product)           
        dictionary = ibm_db.fetch_assoc(stmt1)

    print(carts)  

    return render_template("cart.html",carts=carts)



if __name__ == "__main__":
    app.debug = True
    app.run()    

  