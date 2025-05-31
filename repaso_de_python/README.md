# Trabajo Practico N_2: Repaso de Python

Materia: Programacion 

Ejercicio 1: Ordenación de Productos

Dado un diccionario donde las claves son nombres de productos y los valores son tuplas con (precio, cantidad en stock), escribe un programa que ordene los productos de mayor a menor precio y devuelva una lista ordenada de tuplas con (nombre, precio).
productos = {
    "Laptop": (1200, 5),
    "Smartphone": (800, 10),
    "Tablet": (500, 7),
    "Monitor": (300, 4),
    "Teclado": (50, 20)
}

Ejercicio 2: Agrupación de Datos

Escribe una función que reciba una lista de tuplas con (nombre, edad, ciudad) y devuelva un diccionario donde las claves sean las ciudades y los valores sean listas con los nombres de las personas que viven en esa ciudad.
personas = [
    ("Juan", 25, "Madrid"),
    ("Ana", 30, "Barcelona"),
    ("Luis", 22, "Madrid"),
    ("Elena", 27, "Sevilla"),

    ("Carlos", 35, "Barcelona")
]


Ejercicio 3: Cálculo de Promedios

Crea una función que reciba un diccionario donde las claves sean nombres de estudiantes y los valores sean listas de calificaciones. La función debe devolver un nuevo diccionario con los promedios de cada estudiante redondeados a dos decimales.
calificaciones = {
    "Maria": [85, 90, 78],
    "Jose": [70, 88, 92],
    "Lucia": [95, 85, 87],
    "Pablo": [60, 75, 80]
}


Ejercicio 4: Frecuencia de Palabras

Dado un texto ingresado por el usuario, escribe un programa que cuente la frecuencia de cada palabra y almacene los resultados en un diccionario. La salida debe mostrar las palabras ordenadas de mayor a menor frecuencia.
texto = "python es un lenguaje de programación python es poderoso y versátil"


Ejercicio 5: Unión de Listas de Diccionarios

Escribe una función que reciba dos listas de diccionarios con información de empleados (nombre, cargo, salario). Si un empleado aparece en ambas listas, fusiona la información sumando los salarios. Devuelve una nueva lista con los datos fusionados.
empleados_1 = [
    {"nombre": "Juan", "cargo": "Ingeniero", "salario": 3000},
    {"nombre": "Ana", "cargo": "Diseñadora", "salario": 2500}
]

empleados_2 = [
    {"nombre": "Juan", "cargo": "Ingeniero", "salario": 3200},
    {"nombre": "Carlos", "cargo": "Analista", "salario": 2700}
]


Ejercicio 6: Análisis de Ventas

Dado un diccionario donde las claves son nombres de vendedores y los valores son listas de ventas realizadas en el mes, escribe una función que determine qué vendedor tuvo la mayor suma total de ventas.
ventas = {
    "Pedro": [200, 150, 400],
    "Lucia": [300, 500, 700],
    "Ana": [100, 300, 200]
}


Ejercicio 7: Conversión de Listas a Diccionario

Crea una función que reciba dos listas: una con nombres de personas y otra con sus edades. La función debe devolver un diccionario donde los nombres sean las claves y las edades sean los valores.
nombres = ["Carlos", "Ana", "Pedro", "Marta"]
edades = [28, 34, 25, 40]

Ejercicio 8: Filtrado de Datos

Escribe una función que reciba un diccionario con nombres de ciudades y temperaturas en grados Celsius. La función debe devolver un nuevo diccionario con solo las ciudades donde la temperatura sea superior a 30°C.
temperaturas = {
    "Madrid": 32,
    "Barcelona": 28,
    "Sevilla": 35,
    "Bilbao": 22
}


Ejercicio 9: Cifrado de Texto con Diccionarios

Implementa un cifrado básico donde cada letra de una palabra es reemplazada por otra según un diccionario de mapeo (por ejemplo, {‘a’:’m’, ‘b’:’n’, …}). Escribe una función que cifre y descifre textos usando este diccionario.
cifrado = {
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's',
    'h': 't', 'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z',
    'o': 'a', 'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f', 'u': 'g',
    'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k', 'z': 'l'
}

mensaje = "hola mundo"


Ejercicio 10: Análisis de Encuestas

Se tiene una lista de tuplas donde cada tupla representa la respuesta de un usuario a una encuesta (nombre, edad, respuesta). Escribe una función que devuelva un diccionario donde las claves sean las respuestas y los valores sean listas con los nombres de las personas que eligieron esa respuesta.
respuestas = [
    ("Carlos", 25, "Opción A"),
    ("Ana", 30, "Opción B"),
    ("Pedro", 22, "Opción A"),
    ("Marta", 27, "Opción C"),
    ("Lucia", 35, "Opción B")
]

# Trabajo Practico N_3: Repaso de Python Parte 2

Ejercicio 11: Filtra las películas cuya duración sea mayor a 2 horas y su puntuación superior a 8.0.

peliculas = [
    {"titulo": "Inception", "duracion": 148, "puntuacion": 8.8},
    {"titulo": "El Rey León", "duracion": 88, "puntuacion": 8.5},
    {"titulo": "Interstellar", "duracion": 169, "puntuacion": 8.6},
    {"titulo": "Titanic", "duracion": 195, "puntuacion": 7.8}
]

Ejercicio 12: Agrupa a los estudiantes por curso a partir de una lista de tuplas.

estudiantes = [
    ("Carlos", "Matemáticas"),
    ("Ana", "Historia"),
    ("Luis", "Matemáticas"),
    ("Elena", "Ciencias"),
    ("Marta", "Historia")
]

Ejercicio 13: Cuenta cuántas veces aparece cada letra en una lista de nombres.

nombres = ["Ana", "Juan", "Pedro", "Lucía", "Elena"]

Ejercicio 14: Crea un ranking de jugadores basado en su puntaje total (suma de puntos por nivel).

jugadores = {
    "Player1": [100, 200, 150],
    "Player2": [300, 100, 100],
    "Player3": [50, 150, 300]
}

Ejercicio 15: Transforma una lista de registros en un diccionario usando el identificador como clave.

registros = [
    (101, "Ana", "Biología"),
    (102, "Luis", "Química"),
    (103, "Marta", "Física")
]

Ejercicio 16: Crea un diccionario que indique cuántos productos hay por categoría.

productos = [
    {"nombre": "Manzana", "categoria": "Fruta"},
    {"nombre": "Zanahoria", "categoria": "Verdura"},
    {"nombre": "Pera", "categoria": "Fruta"},
    {"nombre": "Lechuga", "categoria": "Verdura"},
    {"nombre": "Plátano", "categoria": "Fruta"}
]

Ejercicio 17: Fusiona dos listas de precios de productos, quedándote con el precio más bajo para cada producto.

precios_1 = {
    "Arroz": 1.20,
    "Aceite": 3.50,
    "Leche": 0.90
}

precios_2 = {
    "Arroz": 1.10,
    "Leche": 1.00,
    "Pan": 1.30
}


Ejercicio 18: Elimina duplicados de una lista de tuplas manteniendo solo la primera ocurrencia.

transacciones = [
    ("Compra", 100),
    ("Venta", 150),
    ("Compra", 100),
    ("Venta", 150),
    ("Transferencia", 200)
]

Ejercicio 19: Determina el número de empleados por departamento.

empleados = [
    {"nombre": "Carlos", "departamento": "IT"},
    {"nombre": "Ana", "departamento": "HR"},
    {"nombre": "Pedro", "departamento": "IT"},
    {"nombre": "Marta", "departamento": "Marketing"},
    {"nombre": "Lucía", "departamento": "HR"}
]

Ejercicio 20: Agrupa una lista de fechas por año.

fechas = [
    "2022-05-01",
    "2023-03-12",
    "2022-11-30",
    "2024-07-04",
    "2023-09-15"
]
