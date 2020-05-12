from flask import Flask
from pymysql import connect

def read(app):
    @app.route("/R",methods=["GET"])
    def quickSort():
        conn = connect(host='123.56.170.28', port=3306, database='python_db',user='root',password='root')
        cur = conn.cursor()
        sql_str = "select num from number where id <=10;"
        cur.execute(sql_str)
        row_all = cur.fetchall()
        print(row_all)
    # for j in row_all:
    #     c  = str(j).replace("(","").replace(")","").replace("[","").replace("]",'')
    #     d = c.replace("'",'')
    #     k = d.split(",")
    #     for i in range(0,len(k)):
    #         if i ==len(k)-1:
    #             k.remove(k[i])
    #         else:
    #             k[i] = int(k[i])
    #     new_list = quickSort(k)
    #     print(new_list)
    #     sql_str1 = "insert into number2 values" + "(3" + "," + "'"+str(new_list)+"'" + ")"
    #     cur.execute(sql_str1)
    #     conn.commit()