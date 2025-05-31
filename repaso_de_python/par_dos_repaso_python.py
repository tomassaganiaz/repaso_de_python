## Ejercicio 11: Filtrar las Peliculas cuya duracion sea mayor a 2 horas y su puntuacion superior a 8.0

peliculas = [ {"titulo": "Inception", "duracion": 148, "puntuacion": 8.8}, {"titulo": "El Rey León", "duracion": 88, "puntuacion": 8.5}, {"titulo": "Interstellar", "duracion": 169, "puntuacion": 8.6}, {"titulo": "Titanic", "duracion": 195, "puntuacion": 7.8} ]

peliculas_filtradas = [p for p in peliculas if p["duracion"] > 120 and p["puntuacion"] > 8.0]

print(peliculas_filtradas)


## Ejercicio 12: Agrupa a los estudiantes por curso a partir de una lista de tupla

estudiantes = [ ("Carlos", "Matemáticas"), ("Ana", "Historia"), ("Luis", "Matemáticas"), ("Elena", "Ciencias"), ("Marta", "Historia") ]

from collections import defaultdict

# Crear un diccionario con listas para almacenar estudiantes por curso
grupos = defaultdict(list)

# Agrupar estudiantes
for nombre, curso in estudiantes:
    grupos[curso].append(nombre)

# Convertir a diccionario estándar si lo prefieres
grupos = dict(grupos)

print(grupos)

## Ejercicio 13: Cuenta cuantas veces aparece cada letra en una lista de nombre 

nombres = ["Ana", "Juan", "Pedro", "Lucía", "Elena"]

from collections import Counter

# Unir todos los nombres en una sola cadena y contar letras
contador_letras = Counter("".join(nombres))

print(contador_letras)


## Ejercicio 14: Crear un ranking de jugadores basados en su puntaje total (suma de puntos por nivel)

jugadores = "Player1" [100, 200, 150], "Player2" [300, 100, 100], "Player3" [50, 150, 300]

# Calcular la suma de puntos para cada jugador
ranking = {jugador: sum(puntos) for jugador, puntos in jugadores.items()}

# Ordenar jugadores por puntaje de mayor a menor
ranking_ordenado = dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))

print(ranking_ordenado)

## Ejercicio 15: Transfforma una lista de registros en un diccionario usando el identificador como clave

registros = (101, "Ana", "Biología"), (102, "Luis", "Química"), (103, "Marta", "Física")

# Convertir la lista de tuplas en un diccionario
registros_dict = {id: {"nombre": nombre, "materia": materia} for id, nombre, materia in registros}

print(registros_dict)

## Ejercicio 16: Crear un diccionario que indique cuantos productos hay por categoria 

productos = {"nombre": "Manzana", "categoria": "Fruta"}, {"nombre": "Zanahoria", "categoria": "Verdura"}, {"nombre": "Pera", "categoria": "Fruta"}, {"nombre": "Lechuga", "categoria": "Verdura"}, {"nombre": "Plátano", "categoria": "Fruta"}

from collections import defaultdict

# Crear un diccionario para contar productos por categoría
categorias = defaultdict(int)

# Contar productos por categoría
for producto in productos:
    categorias[producto["categoria"]] += 1

# Convertir a un diccionario estándar
categorias = dict(categorias)

print(categorias)

## Ejercicio 17: Fusiona dos listas de precios de productos, quedandote con el precio mas bajo para cada productos

precios_1 = { "Arroz": 1.20, "Aceite": 3.50, "Leche": 0.90 } 
precios_2 = { "Arroz": 1.10, "Leche": 1.00, "Pan": 1.30 }

# Fusionar los diccionarios tomando el precio más bajo
precios_combinados = {}

# Agregar los precios del primer diccionario
for producto, precio in precios_1.items():
    precios_combinados[producto] = precio

# Comparar y agregar los precios del segundo diccionario
for producto, precio in precios_2.items():
    precios_combinados[producto] = min(precios_combinados.get(producto, float('inf')), precio)

print(precios_combinados)


## Ejercicio 18: Elimina duplicados de una lista de tupla manteniendo solo la primera ocurrencia

transacciones = [ ("Compra", 100), ("Venta", 150), ("Compra", 100), ("Venta", 150), ("Transferencia", 200) ]

transacciones_unicas = []
vistos = set()

# Iterar y agregar solo la primera ocurrencia
for transaccion in transacciones:
    if transaccion not in vistos:
        transacciones_unicas.append(transaccion)
        vistos.add(transaccion)

print(transacciones_unicas)

## Ejercicio 19: Determina el numero de empleados por departamentos 

empleados = [ {"nombre": "Carlos", "departamento": "IT"}, {"nombre": "Ana", "departamento": "HR"}, {"nombre": "Pedro", "departamento": "IT"}, {"nombre": "Marta", "departamento": "Marketing"}, {"nombre": "Lucía", "departamento": "HR"} ]

from collections import defaultdict

# Crear un diccionario para contar empleados por departamento
departamentos = defaultdict(int)

# Contar empleados por departamento
for empleado in empleados:
    departamentos[empleado["departamento"]] += 1

# Convertir a un diccionario estándar
departamentos = dict(departamentos)

print(departamentos)

## Ejercicio 20: Agrupa una lista de fecha por año 

fechas = [ "2022-05-01", "2023-03-12", "2022-11-30", "2024-07-04", "2023-09-15" ]

from collections import defaultdict

# Crear un diccionario para agrupar las fechas por año
agrupadas_por_año = defaultdict(list)

# Agrupar fechas por año
for fecha in fechas:
    año = fecha.split("-")[0]  # Extraer el año de la fecha
    agrupadas_por_año[año].append(fecha)

# Convertir a un diccionario estándar si lo prefieres
agrupadas_por_año = dict(agrupadas_por_año)

print(agrupadas_por_año)


