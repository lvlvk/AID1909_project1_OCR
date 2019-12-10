"""
flask，识别服务端
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index_view():
    return render_template("index.html")


@app.route("/faceid", methods=["GET"])
def faceid_view():
    if request.method == "GET":
        fname = request.args.get("filename")
        print(fname)
        dic = locals()
        return render_template("faceid.html", **dic)


@app.route("/ocr", methods=["GET", "POST"])
def ocr_view():
    if request.method == "GET":
        fname = request.args.get("filename")
        print(fname)
        dic = locals()
        return render_template("ocr.html", **dic)


# @app.route("/module")
# def module_view():
#     return render_template("module.html")


if __name__ == '__main__':
    app.run(debug=True)
