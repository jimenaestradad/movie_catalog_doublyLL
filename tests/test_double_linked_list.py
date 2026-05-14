import pytest
from models.node import Node
from models.double_linked_list import DoubleLinkedList


def create_sample_list():
    dll = DoubleLinkedList()
    dll.insert_at_end(Node("Titanic"))
    dll.insert_at_end(Node("Harry Potter"))
    dll.insert_at_end(Node("The Matrix"))
    return dll


def dll_to_list(dll):
    return [node.data for node in dll]


insert_at_beginning_test_cases = [
    ([], ["Avatar"]),
    (["Titanic"], ["Avatar", "Titanic"]),
]

insert_at_end_test_cases = [
    ([], ["Titanic"]),
    (["Harry Potter"], ["Harry Potter", "Titanic"]),
]

search_test_cases = [
    ("Harry Potter", True),
    ("Frozen", False),
]

delete_node_test_cases = [
    (
        ["Titanic", "Harry Potter", "The Matrix"],
        "Harry Potter",
        ["Titanic", "The Matrix"]
    ),

    (
        ["Titanic", "Harry Potter", "The Matrix"],
        "Titanic",
        ["Harry Potter", "The Matrix"]
    ),

    (
        ["Titanic", "Harry Potter", "The Matrix"],
        "The Matrix",
        ["Titanic", "Harry Potter"]
    ),
]

insert_after_node_test_cases = [
    (
        ["Titanic", "Harry Potter", "The Matrix"],
        "Harry Potter",
        "Oppenheimer",
        ["Titanic", "Harry Potter", "Oppenheimer", "The Matrix"]
    ),
]


@pytest.mark.parametrize("initial_list, expected", insert_at_beginning_test_cases)
def test_insert_at_beginning(initial_list, expected):

    dll = DoubleLinkedList()

    for movie in initial_list:
        dll.insert_at_end(Node(movie))

    dll.insert_at_beginning(Node("Avatar"))

    assert dll_to_list(dll) == expected
    assert dll.start.prev is None
    assert dll.end.next is None


@pytest.mark.parametrize("initial_list, expected", insert_at_end_test_cases)
def test_insert_at_end(initial_list, expected):

    dll = DoubleLinkedList()

    for movie in initial_list:
        dll.insert_at_end(Node(movie))

    dll.insert_at_end(Node("Titanic"))

    assert dll_to_list(dll) == expected
    assert dll.start.prev is None
    assert dll.end.next is None


@pytest.mark.parametrize("value, expected_exists", search_test_cases)
def test_search(value, expected_exists):

    dll = create_sample_list()

    result = dll.search(value)

    if expected_exists:
        assert result is not None
        assert result.data == value

    else:
        assert result is None


@pytest.mark.parametrize(
    "initial_list, element_to_delete, expected",
    delete_node_test_cases
)
def test_delete_node(initial_list, element_to_delete, expected):

    dll = DoubleLinkedList()

    for movie in initial_list:
        dll.insert_at_end(Node(movie))

    dll.delete_node(element_to_delete)

    assert dll_to_list(dll) == expected

    if len(dll) > 0:
        assert dll.start.prev is None
        assert dll.end.next is None


@pytest.mark.parametrize(
    "initial_list, reference, new_value, expected",
    insert_after_node_test_cases
)
def test_insert_after_node(initial_list, reference, new_value, expected):

    dll = DoubleLinkedList()

    for movie in initial_list:
        dll.insert_at_end(Node(movie))

    dll.insert_after_node(Node(new_value), reference)

    assert dll_to_list(dll) == expected
    assert dll.start.prev is None
    assert dll.end.next is None

'''Casos de prueba
'''
# 1. Insertar una película al inicio de una lista vacía.
# 2. Insertar una película al inicio de una lista con elementos.
# 3. Insertar una película al final de una lista vacía.
# 4. Insertar una película al final de una lista con elementos.
# 5. Buscar una película existente dentro de la lista.
# 6. Buscar una película que no existe en la lista.
# 7. Eliminar una película ubicada en medio de la lista.
# 8. Eliminar la primera película de la lista.
# 9. Eliminar la última película de la lista.
# 10. Insertar una película después de un nodo específico.