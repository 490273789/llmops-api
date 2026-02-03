from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    result = "Hello"
    result = url_for("show")
    return result


def show_me():
    return "show me"


def show_he():
    return "show he"


app.add_url_rule("/show_me", view_func=show_me)
app.add_url_rule("/show_he", view_func=show_he, endpoint="show")


if __name__ == "__main__":
    app.run()
