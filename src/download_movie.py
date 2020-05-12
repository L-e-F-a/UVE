from flask import Flask, send_from_directory
from flask import request
import random

def download_movie(app):
    @app.route("/download/movie",methods=["GET"])
    def index():
        return send_from_directory(r"../source/",filename="666.flac",as_attachment=True)

