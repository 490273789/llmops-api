from flask import Flask, request

app = Flask(__name__)


@app.route("/create", methods=["POST"])
def create():
    # 接收formData的法师传值
    # 方式1
    # name = request.form.get("name")
    # age = request.form.get("age")
    # 方式2
    name = request.values.get("name")
    age = request.values.get("age")
    return f"name: {name} - age: {age}"


@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("pic")
    fname = f.filename
    with open(f"./imgs/{fname}", "wb") as tf:
        tf.write(f.read())
    return "success"


if __name__ == "__main__":
    app.run()
