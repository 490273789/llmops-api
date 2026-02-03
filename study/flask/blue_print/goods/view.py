from flask import Blueprint, url_for

goods_bp = Blueprint("goods", __name__, url_prefix="/goods")


@goods_bp.route("/list")
def get_list():
    return "List"


@goods_bp.route("/info")
def get_info():
    # 在蓝图中使用url_for或者渲染模版，需要制定蓝图的名字，查找规则是从外向内查找
    print(url_for("goods.get_info"))
    return "Info"
