from pymysql import  connect
import time
import threading
# https://zhuanlan.zhihu.com/p/95578670

# 从score表中查询每个科目的最高分
#
# mysql> SELECT c_name,MAX(grade) FROM score GROUP BY c_name;


sql_1 = """SELECT c_name,MAX(grade) FROM score GROUP BY c_name"""
sql_list = [sql_1]
def seq2(app):
 @app.route("/sq2",methods=["GET"])
 def se122():
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