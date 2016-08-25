from flask import Flask, render_template, url_for, request, redirect
from factory import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        armies_num = int(request.form['armies_num'])
        factory = Factory()
        battlefield = factory.create_battlefield(armies_num)
        return render_template("result.html", result=battlefield.start())


if __name__ == '__main__':
    app.run()