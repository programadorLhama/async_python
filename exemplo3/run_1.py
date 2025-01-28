from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    time.sleep(30)
    return { "hello": "world" }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=False)
