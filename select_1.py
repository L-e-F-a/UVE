from pymysql import  connect
import time
import threading
# https://zhuanlan.zhihu.com/p/95578670
sql_1 = """SELECT * FROM student WHERE department IN ('计算机系','英语系')"""
sql_2 = "SELECT id,name,sex,2013-birth AS age,department,address FROM student  WHERE 2013-birth BETWEEN  18 AND 22;"
sql_3 = "SELECT department, COUNT(id) FROM student GROUP BY department;"
sql_list = [sql_3]

def se1_1():
 try:
    conn = connect(host='123.56.170.28', port=3306, database='good',user='root',password='root')
    cur = conn.cursor()
    while(True):
      for sql in sql_list:
        start = time.time()
        cur.execute(sql)
        row_all = cur.fetchone()
    conn.close()
 except:
     time.sleep(0.5)
     print("1111111111111111111111111111111111111111111111111111111111")
if __name__ =="__main__":
    n =1000
    for i in range(0,n):
        thread_hi = threading.Thread(target=se1_1)
        thread_hi.start()
