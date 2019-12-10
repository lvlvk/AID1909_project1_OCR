from flask import Flask, render_template, request, make_response, redirect, session

app = Flask(__name__)

app.config['SECRET_KEY'] = "YOUR GUESS"
# app.config["DEBUG"] = True

@app.route('/')
def index_view():
    return render_template("h_index.html")

@app.route('/add',methods=["get","post"])
def add_book():
    if request.method == "GET":
        return render_template("add_book.html")
    elif request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        price = request.form.get("price")
        pub = request.form.get("pub")
        # 返回当前函数局部变量
        data = locals()
        return render_template("h_index.html",**data)

@app.route("/demo")
def demo_view():
    # return make_response("你好")

    # return redirect("/")#产生３０２状态码
    resp = make_response("设置cookie成功")
    # resp.set_cookie("uname", "laowang", 3600 * 24 * 30)
    resp.set_cookie("password", "123456", 3600 * 24 * 30)
    return resp

@app.route('/show')
def show_info():
    uname = request.cookies.get("uname")
    password = request.cookies.get("password")
    return "用户名：%s,密码 : %s"%(uname,password)

@app.route('/update/<name>')
def update(name):
    resp = make_response("修改用户名成功")
    resp.set_cookie("uname",name,60*60*24*365)
    return resp

@app.route('/del/<key>')
def del_view(key):
    resp = make_response("删除cookie %s" % key)
    resp.delete_cookie(key)
    return resp

@app.route('/add_session')
def add_session():
    session["isActive"] = True
    session["uname"] = "laowang"
    print(session)
    return "获取session成功"

@app.route("/show_session")
def show_session():
    uname = session["uname"]
    isActive = session["isActive"]
    return "现在%s的状态是%s"%(uname,isActive)

@app.route('/del_session')
def del_session():
    #dic.pop(key)
    #dic.clear()
    del session["isActive"]
    print(session)
    return "删除成功"

@app.route('/xhr')
def xhr_view():
    return render_template("demo01.html")



if __name__ == '__main__':
    app.run(debug=True)