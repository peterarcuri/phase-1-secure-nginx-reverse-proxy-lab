
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Secure backend running behind Nginx reverse proxy", 
        "Client_ip": request.headers.get(
            "X-Forwarded-For",
            request.remote_addr
        ),
        "protocol": request.headers.get(
            "X-Forwarded-Proto",
            "unknown"
        )
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
    