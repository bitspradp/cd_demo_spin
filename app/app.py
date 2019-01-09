from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return "HOST_NAME: "+host_name+" IP_ADDRESS: "+host_ip+"DEPLOYMENT_VERSION: 1.0\n"
    except:
        return "Error"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
