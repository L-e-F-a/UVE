# 查询李四的考试科目（c_name）和考试成绩（grade）
#
# mysql> SELECT c_name, grade
#
#     ->      FROM score WHERE stu_id=
#
#     ->  (SELECT id FROM student
#
#     ->    WHERE name= '李四' );
from pymysql import  connect
import time
import threading
# https://zhuanlan.zhihu.com/p/95578670

sql_1 = """SELECT c_name, grade FROM score WHERE stu_id=(SELECT id FROM student WHERE name= '李四' )"""
sql_list = [sql_1]
def seq3(app):
 @app.route("/sq3",methods=["GET"])
 def seq3():
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