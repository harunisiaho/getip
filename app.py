from flask import Flask,request
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    # host_name = socket.gethostname()
    # host_ip = socket.gethostbyname(host_name)
    host = request.headers.get('Host')
    # return f'<p>Hello World from {host_name} with IP address {host_ip}! from {host}</p>'
    return f'<p>Hello World. Your IP address is  {host.split(':')[0]}</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)