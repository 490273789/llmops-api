from flask import Flask, jsonify, url_for
from flask.views import View

app = Flask(__name__)


# 1. 继承自 - flask.views.View
# 2. 实现dispatch_request
# 3. app.add_url_rule(rule, endpoint, view_func), view_func需要通过ListView.as_view('list')方法转换
# 4. 如果指定了endpoint，在使用url_for反转时必须使用endpoint指定的值，如果没有制定endpoint，那么使用as_view中指定的视图名字来反转
@app.route("/")
def index():
    result = url_for("myList")
    return result


@app.route("/info")
def info():
    result = url_for("show")
    return result


class ListView(View):
    def dispatch_request(self):
        return "hello class view"


def home():
    return "Home"


app.add_url_rule("/home", view_func=ListView.as_view("home"))
app.add_url_rule("/list", view_func=ListView.as_view("myList"))
app.add_url_rule("/show", view_func=ListView.as_view("showList"), endpoint="show")

# 便于测试
# with app.test_request_context():
#     print(url_for("show"))


class BaseView(View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())


class JsonView(BaseView):
    # def post(self):
    #     return
    # def get(self):
    #     return
    def get_data(self):
        return {"name": "wsn", "age": "10"}


class Json2View(BaseView):
    def get_data(self):
        return [{"name": "wsn", "age": "10"}, {"name": "wsz", "age": "20"}]


app.add_url_rule("/json", view_func=JsonView.as_view("json"))
app.add_url_rule("/json2", view_func=Json2View.as_view("json2"))

if __name__ == "__main__":
    app.run()
