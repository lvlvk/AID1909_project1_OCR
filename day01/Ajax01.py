from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/02-temp')
def temp_view():
    return render_template("demo02.html")

@app.route('/02-get')
def Ajax_get():
    return "成功接收请求"


@app.route('/03-temp')
def post_view():
    return render_template("demo03.html")


@app.route('/03-post',methods=["post","get"])
def ajax_post():
    uname = request.form.get("uname")
    age = request.form.get("age")
    return "数据接收成功,姓名%s,年龄%s" %(uname,age)

if __name__ == '__main__':
    app.run()