from flask import Flask, send_from_directory
from flask import request
import random

def login(app):
    @app.route("/login",methods=["GET"])
    def mp():
        if request.method == "GET":
            username = request.args.get("username")
            password = request.args.get("password")
            print(type(username))
            print(username,password)
            if str(username).strip()=="houjunjian" and str(password).strip() =="1234qwer":
                return "欢迎后军舰回来"
            else:
                return "账号或者密码错误"

        else:
            username = request.args.get("username")
            return "22222"
