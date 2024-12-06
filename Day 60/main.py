from flask import Flask, render_template,request
import smtplib
import requests
from config import my_email,my_password

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/About')
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)



@app.route("/post/<int:num>")
def show_post(num):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, my_email, email_msg)


if __name__ == "__main__":
    app.run(debug=True)
