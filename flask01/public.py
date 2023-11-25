from flask import *
from database import *

public = Blueprint("public",__name__)

@public.route("/",methods = ["get","post"])
def register():


    if 'submit' in request.form:
     
     uname = request.form['name']
     paswd = request.form['password']
     email = request.form['email']
     country = request.form['country']
     
     q = "insert into register values(null,'%s','%s','%s','%s')"%(uname,paswd,email,country)
     insert(q)
     return redirect(url_for('public.register'))
    
    return render_template("register.html")
 
@public.route("/login",methods = ['get','post'])
def login():
   if 'submit' in request.form:
     uname = request.form['username']
     passd = request.form['password']
     m="insert into login values(null,'%s','%s','public')"%(uname,passd)
     insert(m)
     return redirect(url_for('public.login'))
   return render_template("login.html")