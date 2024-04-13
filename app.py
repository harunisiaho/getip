from flask import Flask,request
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    host = request.headers.get('Host')
    return f'<p>Hello World. My IP address is  {host.split(':')[0]}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)