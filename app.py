from flask import Flask, render_template, request, redirect, url_for
from models.node import Node
from models.double_linked_list import DoubleLinkedList


# Inicializa Flask y crea la estructura principal del catálogo utilizando Double Linked List.
app = Flask(__name__)

movie_list = DoubleLinkedList()
current_index = 0


# Normaliza títulos ignorando espacios y mayúsculas/minúsculas.
def normalize_title(title):

    return "".join(title.lower().split())


# Ruta principal que renderiza el catálogo y la película actual.
@app.route("/")
def home():

    movies = [node.data for node in movie_list]

    current_movie = None

    if movies:
        current_movie = movies[current_index]

    duplicate_message = request.args.get("message")

    return render_template(
        "index.html",
        movies=movies,
        current_movie=current_movie,
        searched_movie=None,
        search_message=None,
        duplicate_message=duplicate_message
    )


# Agrega nuevas películas validando duplicados dentro de la lista.
@app.route("/add", methods=["POST"])
def add_movie():

    movie_title = request.form.get("title", "").strip()

    if movie_title:

        normalized_new_title = normalize_title(movie_title)

        existing_movie = None

        for node in movie_list:

            if normalize_title(node.data) == normalized_new_title:
                existing_movie = node
                break

        if existing_movie is None:
            movie_list.insert_at_end(Node(movie_title))
            return redirect("/")

        return redirect(url_for(
            "home",
            message=f"Movie '{movie_title}' already exists in your list."
        ))

    return redirect("/")


# Elimina películas utilizando delete_node() y actualiza la navegación actual.
@app.route("/delete", methods=["POST"])
def delete_movie():

    global current_index

    movie_title = request.form.get("title", "").strip()

    if movie_title:

        actual_movie = None

        for node in movie_list:

            if normalize_title(node.data) == normalize_title(movie_title):
                actual_movie = node.data
                break

        if actual_movie is not None:

            movie_list.delete_node(actual_movie)

            if len(movie_list) == 0:
                current_index = 0

            elif current_index > len(movie_list) - 1:
                current_index = len(movie_list) - 1

    return redirect("/")


# Navega hacia la película anterior utilizando current_index.
@app.route("/previous")
def previous_movie():

    global current_index

    if current_index > 0:
        current_index -= 1

    return redirect("/")


# Navega hacia la siguiente película utilizando current_index.
@app.route("/next")
def next_movie():

    global current_index

    if current_index < len(movie_list) - 1:
        current_index += 1

    return redirect("/")


# Busca películas dentro del catálogo utilizando el método search().
@app.route("/search", methods=["POST"])
def search_movie():

    movie_title = request.form.get("search_title", "").strip()

    movies = [node.data for node in movie_list]

    current_movie = None

    if movies:
        current_movie = movies[current_index]

    searched_movie = None
    search_message = None

    if movie_title:

        result = None

        for node in movie_list:

            if normalize_title(node.data) == normalize_title(movie_title):
                result = node
                break

        if result is not None:
            searched_movie = result.data

        else:
            search_message = f"Movie '{movie_title}' not found."

    return render_template(
        "index.html",
        movies=movies,
        current_movie=current_movie,
        searched_movie=searched_movie,
        search_message=search_message,
        duplicate_message=None
    )

if __name__ == "__main__":
    app.run(debug=True)