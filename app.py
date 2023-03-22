from flask import Flask
from flask import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'FBGM'

@app.route("/<lover>")
def who_do_ya_love(lover):
    if escape(lover) == "caitlyn":
        return f"I love {escape(lover)}!"
    else:
        return "That's not my lover!"