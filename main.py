from flask import Flask, render_template, request
import requests
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("static/assets/img/post_img") if isfile(join("static/assets/img/post_img", f))]

app = Flask(__name__)

# response = requests.get("https://api.npoint.io/88c2c1f644ef334058be")
# data = response.json()

blog = 0


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/88c2c1f644ef334058be")
    data = response.json()

    return render_template("index.html", all_posts=data)


@app.route("/index")
def index():
    response = requests.get("https://api.npoint.io/88c2c1f644ef334058be")
    data = response.json()
    return render_template("index.html", all_posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form

        s='<h1>Successfully sent your message</h1>'
        return f"{s}"
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<num>")
def get_post(num):
    global blog
    response = requests.get("https://api.npoint.io/88c2c1f644ef334058be")
    data = response.json()

    for item in data:
        print(item)
        print(item["id"])
        if item["id"] == int(num):
            blog = item
            print(blog)
    return render_template("post.html", posts=blog)






app.run(debug=True)
