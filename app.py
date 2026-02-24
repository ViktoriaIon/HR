from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)


CONSULT = {1: "Анна Иванова", 2: "Олег Петров", 3: "Мария Сидорова"}


CONSULT1 = {
    1: "Консультант Анна чудесно работает с выгоранием",
    2: "Помогает победить прокрастинацию и начать работать",
    3: "Выслушивает жалобы на руководство",
}


@app.route("/")
def consult():
    return render_template("index.html", buttons=CONSULT)


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def consult1():
    return render_template("index.html", text=CONSULT1)


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def cons1():
    return render_template("cons1.html")


if __name__ == "__main__":
    app.run(debug=True)
