from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from flask import Flask,request
import socket

app = Flask(__name__)

xray_recorder.configure(service='Get IP Application')
XRayMiddleware(app, xray_recorder)

@app.route('/')
def hello_world():
    host = request.headers.get('Host')
    return f'<p>Hello World. My IP address is  {host.split(':')[0]}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)