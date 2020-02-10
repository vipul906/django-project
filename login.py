#!/usr/bin/python
import cgi,cgitb
cgitb.enable()
import MySQLdb
import json
print "Content-type:text/html\n\n"

class mysite:

    def __init__(self):
        pass

    def dbconnection(self):
       conn = MySQLdb.connect("localhost","root","tas123","mydb_vipul")
       curr = conn.cursor()
       return conn, curr

    def signup(self,username,password,email):
        conn, curr = self.dbconnection()
        #sql = "INSERT INTO logindata(username,password) VALUES ('admin','admin123')"
        sql = "select username,password from logindata where username='%s'"%username
        curr.execute(sql)
        if curr.fetchone():
              return 'username is already exsit'
        
        sql = "INSERT INTO logindata(username,password,Email) VALUES ('%s','%s','%s')"%(username,password,email)
        curr.execute(sql)
        conn.commit()
        #print curr.fetchall()
        #print curr.rowcount,'record inserted'
        #except:
        #    conn.rollback()
        conn.close()
        return 'Username and password is created. Now u can login'

    def signin(self,username,password):
        conn, curr = self.dbconnection()
        sql = "select username,password from logindata where username='%s'"%username
        #print sql
        curr.execute(sql)
        if not curr.fetchone(): return 'username is worng'
        userpwd_data = curr.fetchone()
        #userpwd_dict = {}
        #userpwd_dict = dict(userpwd_data)
        conn.close()
        #print userpwd_data
        if  userpwd_data[1] == password:
           return 'Detail are correct'
        return 'password is worng'
                

if __name__ == "__main__":

    form = cgi.FieldStorage()
    username = form.getvalue('user')
    obj = mysite()
    password = form.getvalue('pwd')
    email = form.getvalue('email')
    login  = form.getvalue('login')
    if login == 'signin' : print json.dumps(obj.signin(username,password))
    if login == 'signup' : print json.dumps(obj.signup(username,password,email))
