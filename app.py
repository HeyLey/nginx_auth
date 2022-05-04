from flask import Flask, render_template, request, session, redirect, url_for
import logging

app = Flask(__name__)
log_level = logging.INFO

@app.route('/')
def nginx_auth():
   # if 'X-Juddling' in request.headers:
    return render_template("info.html"), 200
#    else:
 #       return "Error", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)