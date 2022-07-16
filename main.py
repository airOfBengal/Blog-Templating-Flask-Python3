import requests as requests
from flask import Flask, render_template


app = Flask(__name__)
blog_url = "https://api.npoint.io/bebcf92ccec102dc80d3"


def get_blogs():
    response = requests.get(blog_url)
    return response.json()


@app.route('/')
def home():
    global blogs
    blogs = get_blogs()
    return render_template("index.html", blogs=blogs)


@app.route('/post/<int:num>')
def post(num):
    blog = [blog for blog in blogs if blog["id"] == num][0]
    return render_template('post.html', post=blog)


if __name__ == "__main__":
    app.run(debug=True)
