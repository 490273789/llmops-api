from flask import Flask, render_template

# 自定一模版文件夹
# app = Flask(__name__, template_folder="temp")
# 修改静态文件默认位置
# app = Flask(__name__, static_folder="static2")
app = Flask(__name__)


@app.template_filter("cut")
def cut(value):
    value = value.replace("老太太", "阿姨")


# MVT - T - Template
# 默认获取templates文件夹下的文件
@app.route("/index/<int:id>")
def index(id):
    context = {
        "name": "wsn",
        "age": "18",
        "price": "10.5",
        "nick_name": "",
        "code": "<script>alert('Hello')</script>",
        "hobby": ["python", "java", "javascript", "rust", "go"],
        "card": {"name": "BOC", "no": "20298888888", "city": "BJ"},
    }
    return render_template("index1.html", **context)


# 模版中使用url_for
@app.route("/home")
def home():
    return render_template("children.html")


if __name__ == "__main__":
    app.run()
