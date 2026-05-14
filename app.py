from flask import Flask, render_template, request, redirect
from models.node import Node
from models.double_linked_list import DoubleLinkedList

app = Flask(__name__)

movie_list = DoubleLinkedList()
current_index = 0


@app.route("/")
def home():
    movies = [node.data for node in movie_list]

    current_movie = None
    if movies:
        current_movie = movies[current_index]

    return render_template(
        "index.html",
        movies=movies,
        current_movie=current_movie
    )


@app.route("/add", methods=["POST"])
def add_movie():
    movie_title = request.form.get("title")

    if movie_title:
        movie_list.insert_at_end(Node(movie_title))

    return redirect("/")


@app.route("/previous")
def previous_movie():
    global current_index

    if current_index > 0:
        current_index -= 1

    return redirect("/")


@app.route("/next")
def next_movie():
    global current_index

    if current_index < len(movie_list) - 1:
        current_index += 1

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)