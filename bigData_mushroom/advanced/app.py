from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"
@app.route("/postmethod")
def hope():
    return "Nope"

if (__name__ == "__main__"):
    app.run(debug = True, port = 1207)
