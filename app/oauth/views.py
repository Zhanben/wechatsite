from . import login


@login.route("/login", methods=["GET"])
def index():
    return "login success!\n"
