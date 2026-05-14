from flask import Flask, render_template, request, redirect
from models.node import Node
from models.double_linked_list import DoubleLinkedList

app = Flask(__name__)

movie_list = DoubleLinkedList()


@app.route("/")
def home():

    movies = [node.data for node in movie_list]

    return render_template("index.html", movies=movies)


@app.route("/add", methods=["POST"])
def add_movie():

    movie_title = request.form.get("title")

    if movie_title:
        movie_list.insert_at_end(Node(movie_title))

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)