"""
服务端
"""
from datetime import timedelta
from flask import *

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(seconds=1)


@app.route("/")
def index_view():
    return render_template("index.html")


@app.route("/search")
def search_view():
    search = request.args.get()
    # 进入数据查询
    return "返回查询结果"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7788)