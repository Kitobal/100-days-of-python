from flask import Flask, render_template

import requests


app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()




@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/About')
def about():
    return render_template("about.html")


@app.route('/Contact')
def contact():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def show_post(num):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
