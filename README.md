# Catálogo de Películas utilizando una Doubly Linked List (Non-Circular)

## por

María Jimena Estrada – 20250126

---

# Descripción del Proyecto

Este proyecto consiste en una aplicación de catálogo de películas desarrollada en Python utilizando una **Doubly Linked List (Non-Circular)** implementada completamente desde cero.

La aplicación permite al usuario:

* Agregar películas al catálogo.
* Navegar entre películas.
* Buscar películas.
* Eliminar películas.
* Evitar películas duplicadas.

La interfaz gráfica fue desarrollada utilizando:

* Flask
* HTML
* CSS

El objetivo principal del proyecto es demostrar el funcionamiento de una Doubly Linked List no circular en un caso de uso real mediante una interfaz visual e interactiva.

---

# Estructura de Datos Utilizada

## Doubly Linked List (Non-Circular)

Una Doubly Linked List es una estructura de datos lineal dinámica en la cual cada nodo almacena:

* Data
* Referencia al nodo siguiente (`next`)
* Referencia al nodo anterior (`prev`)

Esta implementación es **no circular**, lo que significa que:

* El primer nodo apunta a `None` en `prev`
* El último nodo apunta a `None` en `next`

Esto permite navegación bidireccional manteniendo un inicio y un final definidos.

---

# Funcionalidades Principales

## 1. Agregar películas

El usuario puede agregar nuevas películas al catálogo.

## 2. Validación de películas duplicadas

El sistema evita películas repetidas ignorando:

* Mayúsculas y minúsculas
* Espacios adicionales

Ejemplo:

* Harry Potter
* harrypotter
* HARRY POTTER

Son consideradas la misma película.

## 3. Buscar películas

El usuario puede buscar películas dentro del catálogo utilizando la funcionalidad de búsqueda implementada.

## 4. Eliminar películas

Las películas pueden eliminarse dinámicamente del catálogo.

## 5. Navegación Previous / Next

El usuario puede navegar entre películas utilizando botones de previous y next.

---

# Tecnologías Utilizadas

* Python3
* Flask
* HTML
* CSS
* Pytest
* GitHub & GitKraken

---

# Estructura del Proyecto

```bash
movie_catalog_doublyLL/
│
├── app.py
├── models/
│   ├── node.py
│   └── double_linked_list.py
│
├── tests/
│   └── test_double_linked_list.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── README.md
└── .gitignore
```

---

# Complejidad Temporal de los Métodos Principales

| Método                | Complejidad |
| --------------------- | ----------- |
| insert_at_beginning() | O(1)        |
| insert_at_end()       | O(1)        |
| search()              | O(n)        |
| delete_node()         | O(n)        |
| insert_after_node()   | O(n)        |
| traversal / iteration | O(n)        |

---

# Unit Testing

El proyecto incluye unit testing utilizando **pytest**.

Se implementaron un mínimo de 10 escenarios de prueba para validar:

* Inserciones
* Búsquedas
* Eliminaciones
* Inserciones después de nodos
* Comportamiento no circular de la estructura

---

# Instalación y Ejecución

## 1. Clonar el repositorio

```bash
git clone <https://github.com/jimenaestradad/movie_catalog_doublyLL >
```

---

## 2. Entrar a la carpeta del proyecto

```bash
cd movie_catalog_doublyLL
```

---

## 3. Instalar Flask

```bash
python3 -m pip install flask
```

---

## 4. Instalar Pytest

```bash
python3 -m pip install pytest
```

---

# Ejecutar la Aplicación

Ejecutar Flask utilizando:

```bash
python3 app.py
```

Luego abrir:

```bash
http://127.0.0.1:5000
```

en el navegador.

---

# Ejecutar Unit Tests

Ejecutar los tests de forma local utilizando:

```bash
python3 -m pytest -v
```

---
