from flask import Flask, request
import time

app = Flask(__name__)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.route("/")
def measure_latency():
    # Calculate latency in milliseconds
    latency_ms = (time.time() - request.start_time) * 1000
    client_ip = request.remote_addr
    return f"Your IP: {client_ip}\nLatency: {latency_ms:.2f} ms\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
