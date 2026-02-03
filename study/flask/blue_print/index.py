from flask import Flask
from goods import goods_bp
from user import user_bp

app = Flask(__name__)


# 注册蓝图
app.register_blueprint(goods_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run()
