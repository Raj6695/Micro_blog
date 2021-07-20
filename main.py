from flask import Flask, render_template, request
import requests
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("static/assets/img/post_img") if isfile(join("static/assets/img/post_img", f))]

app = Flask(__name__)

OWN_EMAIL =  EMAIL ADDRESS
OWN_PASSWORD = PASSWORD

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
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

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
