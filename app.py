from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to my API"}
@app.route("/health")
def health():
    return {"status": "ok"}
@app.route("/info")
def info():
    return{
        "name": "python-ci-cd-demo",
        "version": "1.0.0"
        }
            


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)