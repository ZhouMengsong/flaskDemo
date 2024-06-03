from app.web import wb


@wb.route("/")
def index():
    return "hello word"

