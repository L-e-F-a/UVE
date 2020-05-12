from flask import Flask
from random import randint
from pymysql import connect
import time

def inserts(app):
  @app.route("/INSERT",methods=["GET"])
  def insert():
    conn = connect(host='123.56.170.28', port=3306, database='python_db',user='root',password='root')
    cur = conn.cursor()
    start_time = time.time()
    for j in range(1000):
        li_1 = []
        for i in range(10000):
            li_1.append(randint(1,10000))
        sql_str = "insert into number values" + "(" + str(j+1) + "," + "'"+str(li_1) +"'"+ ")" +";"
        cur.execute(sql_str)
    conn.commit()
    stop_time = time.time()
    print(stop_time - start_time)