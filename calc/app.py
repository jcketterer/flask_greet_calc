# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    sum = add(a, b)
    return str(sum)


@app.route("/sub")
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    answer = sub(a, b)
    return str(answer)


@app.route("/mult")
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    product = mult(a, b)
    return str(product)


@app.route("/div")
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    answer = div(a, b)
    return str(answer)


# Part Two

operations = {"add": add, "sub": sub, "mult": mult, "div": div}


@app.route("/math/<oper>")
def all_math(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answers = operations[oper](a, b)
    print(answers)
    return str(answers)
