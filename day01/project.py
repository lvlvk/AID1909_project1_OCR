from flask import Flask, render_template, request
from security_data import DatabaseModel
app = Flask(__name__)
db = DatabaseModel(user='root', password='123456', database='security')

@app.route("/",methods=["post","get"])
def index_view():
    return render_template("index.html")



@app.route('/add_person',methods=["post","get"])
def add_person():
    if request.method == "GET":
        return render_template("add_person.html")
    elif request.method == "POST":
        nature = request.form.get("nature")
        uname = request.form.get("uname")
        tel = request.form.get("tel")
        adress = request.form.get("adress")

        db = DatabaseModel(user='root', password='123456', database='security')
        re = db.check_car("浙A323UU", "in")
        print(re)

        if nature == "owners":
            return "业主%s登记成功" %uname
        elif nature == "visiters":
            return "访客%s登记成功" %uname

@app.route('/dict')
def dict():

    re = db.check_car("浙A323UU", "in")
    print(re)
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)































@app.route('/exercise-temp')
def exercise_temp():
    return render_template("exercise-get.html")

@app.route('/exercise-get')
def exercise_get():
    search = request.args.get("search")
    return "显示和%s有关的内容"%search

@app.route('/post_temp')
def post_temp():
    return render_template("exercise-post.html")

@app.route('/get-post',methods=["post"])
def get_post():
    uname = request.form.get("uname")
    upwd = request.form.get("upwd")

    return "欢迎%s" %uname






if __name__ == '__main__':
    app.run(debug=True)

