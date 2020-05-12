from flask import Flask, send_from_directory
from flask import request
import random
app = Flask(__name__)
def get_ssq_num(app):
    @app.route("/SSQ",methods=["GET"])
    def SSQ():
        list_hong = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
        list_blue = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        list_final = random.sample(list_hong,6)
        list_final.sort()
        re = "红球*** "+ str(list_final)+ "***" + "蓝球*** "+str(random.sample(list_blue,1))+"***"
        return re

