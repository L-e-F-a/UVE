from pymysql import  connect
import time
import threading
# https://zhuanlan.zhihu.com/p/95578670

sql_1 = """SELECT student.id, name,sex,birth,department, address, c_name,grade FROM student, score WHERE address LIKE '湖南%' AND student.id=score.stu_id"""
sql_list = [sql_1]
def seq10(app):
 @app.route("/sq10",methods=["GET"])
 def se1e1():
   try:
    conn = connect(host='123.56.170.28', port=3306, database='good',user='root',password='root')
    cur = conn.cursor()
    for sql in sql_list:
        start = time.time()
        cur.execute(sql)
        row_all = cur.fetchone()
    conn.close()
    return row_all
   except Exception as e:
     time.sleep(0.5)
     print(e)