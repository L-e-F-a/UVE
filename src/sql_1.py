from pymysql import  connect
import time
import threading
# https://zhuanlan.zhihu.com/p/95578670
sql_1 = """SELECT * FROM student WHERE department IN ('计算机系','英语系')"""
sql_list = [sql_1]
def seq1(app):
 @app.route("/sq1",methods=["GET"])
 def se1_1():
   try:
    conn = connect(host='123.56.170.28', port=3306, database='good',user='root',password='root')
    cur = conn.cursor()
    for sql in sql_list:
        start = time.time()
        cur.execute(sql)
        row_all = cur.fetchone()
    conn.close()
    return 'ok'
   except Exception as e:
     time.sleep(0.5)
     print(e)

