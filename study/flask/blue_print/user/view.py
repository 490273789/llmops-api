from flask import Blueprint

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("login")
def login():
    return "Login"


@user_bp.route("logout")
def logout():
    return "Logout"
