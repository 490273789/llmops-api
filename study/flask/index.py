# import json
# import os
from datetime import timedelta

from flask import (
    Flask,
    current_app,
    g,
    make_response,
    redirect,
    request,
    session,
    url_for,
)

# 使用了下面这个库处理路由参数的类型
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 在外部使用上下文的添加方法1
# app_ctx = app.app_context()
# app_ctx.push()
# 方法2 仅作用域内生效
# with app.app_context():
#     print(f"{current_app.name}")

app.config.secret_key = "casdcasdascd"

# 设置session的有效期为两天
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=2)

# cookie 为了解决http无状态的问题，来记录用户信息
# 浏览器对cookie有限制，数量最好保证在20～30个，大小小于4k
# cookie的过期时间，如果不设置，会在浏览器关闭时过期
# max_age 单位时秒
# expries 类型为datetime，这个时间为格林尼治时间，对比北京时间会自动+8小时
#  max_age优先级更高


# session - 存储在服务器上，出现原因是解决cookie存储数据不安全的问题
# secret_key更换，之前的session id将全部过期
@app.context_processor
# 操作cookie
@app.route("/index")
def index():
    # Flask全局对象g, 需要再有当前对象上下文的地方使用
    print(f"g: {g}")
    # 获取应用上下文
    print(f"current_app: {current_app.name}")
    session["token"] = "session"
    # 设置session的持久化，默认增加31天
    # session.permanent = True
    resp = make_response("设置 cookie")
    resp.set_cookie("uname", "wsn")
    return resp


# 获取cookie
@app.route("/get_cookie")
def get_cookie():
    uname = request.cookies.get("uname")
    token = session.get("token")
    return f"cookie: {uname}, token: {token}"


# 删除cookie
@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("设置 cookie")
    resp.delete_cookie("uname", "wsn")
    session.pop("token")
    # clear 清空session信息在: session.clear()
    return resp


# 动态路由


# 参数类型转换 converter:variable
# converter可以是以下几种类型
# string: 默认为string
# int
# float
# path: 可以是带斜杠的字符串
# uuid
# any: 可以在url中指定多个路径
@app.route("/article/<int:id>")
def get_article(id):
    return f"{id}"


# path
@app.route("/path/<path:id>")
def get_path(id):
    # 1/2/3
    return f"{id}"


# any
@app.route("/<any(user, item):path>/<int:id>")
def get_any(path, id):
    if path == "user":
        return f"{path}: {id}"
    elif path == "item":
        return f"{path}: {id}"
    return f"{id}"


# 自定义参数类型
class PhoneConverter(BaseConverter):
    regex = r"^1[3-9]\d{9}$"


# 注册自定义类型
app.url_map.converters["phone"] = PhoneConverter


# path
@app.route("/phone/<phone:param>")
def phone(param):
    return f"{param}"


# 自定义参数处理
class ItemConverter(BaseConverter):
    def to_python(self, value):
        return value.split("+")


app.url_map.converters["li"] = ItemConverter


@app.route("/info/<li:item>")
def info(item):
    return f"item: {item}"


# 通过路径传递参数有利于SEO的优化
# 处理查询参数
@app.route("/user")
def get_user():
    # 方法1
    # user_name = request.args.get("user_name")
    # pwd = request.args.get("pwd")
    # 方法2
    user_name = request.values.get("user_name")
    pwd = request.values.get("pwd")
    return f"{user_name} - {pwd}"


# url_for
# 作用：
# 1. 项目重构的时候修改路由地址，可用这个方法兼容
# 2. 会转义一些特殊字符和unicode字符串
@app.route("/show_url")
def show_url():
    url = url_for(
        "get_user"
    )  # 第二个参数默认开始匹配路径参数，匹配不上默认已查询参数的形式传递
    return f"{url}"


# 重定向
@app.route("/detail")
def login():
    return redirect("/index", code=301)


class Config:
    DEBUG = True


# 返回格式
@app.route("/html")
def html(id):
    return "hello"  # 实际返回的是html


# 添加配置禁止中文转换为ascii
app.config["JSON_AS_ASCII"] = False


@app.route("/json")
def r_json():
    return {"name": "王sn"}


# 元组第一个参数是响应的内容，第二个参数可以是状态码、可以是headers
@app.route("/tuple")
def r_tuple():
    # return 'tuple', 202
    # return "tuple", {"cus-header": "python"}
    # return "tuple", 202, {"cus-header": "python"}
    return "tuple", 202, [("cus-header", "python")]


# 自定义响应对象
@app.route("/response")
def r_response():
    # return Response("你好", status=202, headers={"cus-header": "python"})
    resp = make_response("这个是创建的Response对象")
    resp.headers["cus-header"] = "python"
    resp.status = 666
    return resp


if __name__ == "__main__":
    # 添加配置的几种方式
    # shell中通过命令启动，也可以穿入参数：flask run -p 8000 --debug
    # app.run(debug=True) # 开启debug模式
    # app.config["DEBUG"] = True
    # app.config.update({"DEBUG": True})
    # app.config.from_mapping({"DEBUG": True})
    # app.config.from_object(Config)
    # app.config.from_file("config.json", json.load)
    # app.config.from_pyfile("settings.py")

    # os.environ["flask_settings"] = "settings.py"
    # app.config.from_envvar("flask_settings")

    # print(f"DEBUG_ENV:{os.environ}")
    # print(f"DEBUG_ENV:{os.environ.get('FLASK_DEBUG')}")

    app.run()
