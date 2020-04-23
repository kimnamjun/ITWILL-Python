from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/room')
def room():
    return render_template("/room.html")

@app.route('/create')
def create():

    return render_template("/index.html")

if __name__ == "__main__":
    app.run()