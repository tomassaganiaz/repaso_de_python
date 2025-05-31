## Ejercicio 1: Ordenacion de Productos


# Diccionario de productos
productos = {
    "Laptop": (1200, 5),
    "Smartphone": (800, 10),
    "Tablet": (500, 7),
    "Monitor": (300, 4),
    "Teclado": (50, 20)
}

# Ordenar los productos por precio (índice 0 de la tupla), en orden descendente
productos_ordenados = sorted(productos.items(), key=lambda x: x[1][0], reverse=True)

# Transformar la lista para mostrar solo el nombre y el precio
resultado = [(nombre, precio) for nombre, (precio, _) in productos_ordenados]

# Imprimir resultado
print(resultado)


## Ejercicio 2: Agrupacion de Datos 


def agrupar_por_ciudad(lista_personas):
    resultado = {}
    for nombre, edad, ciudad in lista_personas:
        if ciudad not in resultado:
            resultado[ciudad] = []
        resultado[ciudad].append(nombre)
    return resultado

# Lista de personas
personas = [
    ("Juan", 25, "Madrid"),
    ("Ana", 30, "Barcelona"),
    ("Luis", 22, "Madrid"),
    ("Elena", 27, "Sevilla"),
    ("Carlos", 35, "Barcelona")
]

# Llamada a la función
diccionario_ciudades = agrupar_por_ciudad(personas)

# Imprimir resultado
print(diccionario_ciudades)


# Ejercicio 3: Calculo de Promedios 


def calcular_promedios(calificaciones):
    return {nombre: round(sum(notas) / len(notas), 2) for nombre, notas in calificaciones.items()}

# Diccionario de calificaciones
calificaciones = {
    "Maria": [85, 90, 78],
    "Jose": [70, 88, 92],
    "Lucia": [95, 85, 87],
    "Pablo": [60, 75, 80]
}

# Llamada a la función
promedios = calcular_promedios(calificaciones)

# Imprimir resultado
print(promedios)



## Ejecicio 4: Frecuencia de Palabras 


from collections import Counter

# Texto de entrada
texto = "python es un lenguaje de programación python es poderoso y versátil"

# Convertir el texto a minúsculas y dividirlo en palabras
palabras = texto.lower().split()

# Contar la frecuencia de cada palabra
frecuencia = Counter(palabras)

# Ordenar las palabras por frecuencia en orden descendente
resultado = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

# Imprimir resultado
print(resultado)


## Ejercicio 5: Union de Listas de Diccionarios 


def fusionar_empleados(lista1, lista2):
    empleados_dict = {}

    # Procesar la primera lista
    for empleado in lista1:
        nombre = empleado["nombre"]
        empleados_dict[nombre] = empleado

    # Procesar la segunda lista
    for empleado in lista2:
        nombre = empleado["nombre"]
        if nombre in empleados_dict:
            empleados_dict[nombre]["salario"] += empleado["salario"]
        else:
            empleados_dict[nombre] = empleado

    # Convertir el diccionario de vuelta a una lista
    return list(empleados_dict.values())

# Listas de empleados
empleados_1 = [
    {"nombre": "Juan", "cargo": "Ingeniero", "salario": 3000},
    {"nombre": "Ana", "cargo": "Diseñadora", "salario": 2500}
]

empleados_2 = [
    {"nombre": "Juan", "cargo": "Ingeniero", "salario": 3200},
    {"nombre": "Carlos", "cargo": "Analista", "salario": 2700}
]

# Llamada a la función
empleados_fusionados = fusionar_empleados(empleados_1, empleados_2)

# Imprimir resultado
print(empleados_fusionados)


## Ejercicio 6: Analisis de Ventas 


def mejor_vendedor(ventas):
    return max(ventas.items(), key=lambda x: sum(x[1]))

# Diccionario de ventas
ventas = {
    "Pedro": [200, 150, 400],
    "Lucia": [300, 500, 700],
    "Ana": [100, 300, 200]
}

# Llamada a la función
vendedor_top = mejor_vendedor(ventas)

# Imprimir resultado
print(f"El mejor vendedor es {vendedor_top[0]} con un total de {sum(vendedor_top[1])} en ventas.")


## Ejercicio 7: Conversion de Lista a Diccionario 


def convertir_a_diccionario(nombres, edades):
    return dict(zip(nombres, edades))

# Listas de nombres y edades
nombres = ["Carlos", "Ana", "Pedro", "Marta"]
edades = [28, 34, 25, 40]

# Llamada a la función
diccionario_resultante = convertir_a_diccionario(nombres, edades)

# Imprimir resultado
print(diccionario_resultante)


## Ejercicio 8: Filtrado de Datos 


def filtrar_ciudades(temperaturas):
    return {ciudad: temp for ciudad, temp in temperaturas.items() if temp > 30}

# Diccionario de temperaturas
temperaturas = {
    "Madrid": 32,
    "Barcelona": 28,
    "Sevilla": 35,
    "Bilbao": 22
}

# Llamada a la función
ciudades_filtradas = filtrar_ciudades(temperaturas)

# Imprimir resultado
print(ciudades_filtradas)


## Ejecicio 9: Cifrado de Texto con Diccionarios


def cifrar_texto(texto, mapeo):
    return "".join(mapeo.get(letra, letra) for letra in texto.lower())

def descifrar_texto(texto, mapeo):
    inverso_mapeo = {v: k for k, v in mapeo.items()}
    return "".join(inverso_mapeo.get(letra, letra) for letra in texto.lower())

# Diccionario de cifrado
cifrado = {
    'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's',
    'h': 't', 'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z',
    'o': 'a', 'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f', 'u': 'g',
    'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k', 'z': 'l'
}

# Mensaje a cifrar
mensaje = "hola mundo"

# Cifrar y descifrar el mensaje
mensaje_cifrado = cifrar_texto(mensaje, cifrado)
mensaje_descifrado = descifrar_texto(mensaje_cifrado, cifrado)

# Imprimir resultados
print(f"Mensaje cifrado: {mensaje_cifrado}")
print(f"Mensaje descifrado: {mensaje_descifrado}")


## Ejercicio 10: Analisis de Encuestas 


def agrupar_respuestas(respuestas):
    resultado = {}
    for nombre, edad, respuesta in respuestas:
        if respuesta not in resultado:
            resultado[respuesta] = []
        resultado[respuesta].append(nombre)
    return resultado

# Lista de respuestas
respuestas = [
    ("Carlos", 25, "Opción A"),
    ("Ana", 30, "Opción B"),
    ("Pedro", 22, "Opción A"),
    ("Marta", 27, "Opción C"),
    ("Lucia", 35, "Opción B")
]

# Llamada a la función
diccionario_respuestas = agrupar_respuestas(respuestas)

# Imprimir resultado
print(diccionario_respuestas)
