from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return render_template(
        'index.html',
        message="🚀 Welcome to Joshua's DevOps Flask App — Deployed with CI/CD Pipeline!",
        host_name=hostname
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
