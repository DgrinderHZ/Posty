from flask import Flask, render_template
from store import Post, PostStore
app = Flask(__name__)

dummy_posts = [
    Post(id=1,
         photo_url='https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=50&w=50',
         name='Sara',
         body='Lorem Ipsum'),
    Post(id=2,
         photo_url='https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
         name='John',
         body='Lorem Ipsum'),
]
post_store = PostStore()
post_store.add(dummy_posts[0])
post_store.add(dummy_posts[1])

@app.route("/")
def home():
    return render_template("index.html", posts = post_store.get_all())

app.run()
