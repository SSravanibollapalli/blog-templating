from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    response_blog = requests.get(blog_url)  # Move the API request here
    all_posts = response_blog.json()
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<num>")
def blog(num):
    response_blog = requests.get(blog_url)  # Move the API request here as well
    chose_post = response_blog.json()[int(num) - 1]
    return render_template("post.html", post=chose_post)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
