from flask import *
import pymysql
import os

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='static/images'

@app.route("/api/sign_in",methods=['POST'])
def signup():
    # code to execute
    user_name=request.form('user_name')
    user_contact=request.form('user_contact')
    user_email=request.form('user_email')
    date_of_birth=request.form('date_of_birth')
    password=request.form('password')

    print(user_name,user_contact,user_email,date_of_birth,password)
    # create a connection
    connection=pymysql.connect(host=,user=,password=,database=)

    # cursor
    cursor=connection.cursor()

    sql='insert into users(user_name,user_contact,user_email,date_of_birth,password) values(%s,%s,%s,%s,%s)'
    data=user_name,user_contact,user_email,date_of_birth,password

    cursor.execute(sql,data)

    connection.commit()


@app.route("/api/login",methods=['POST'])
def login():
    # code to execute
    user_name=request.form('user_name')
    user_email=request.form('user_email')
    password=request.form('password')
    
    print(user_name,user_email)

    connection=pymysql.connect(host='localhost',user=,database=,passwd=,)



