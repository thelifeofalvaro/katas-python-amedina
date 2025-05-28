# Kata 1. Enunciado: Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
#Definimos cadena de prueba:
cadena = "Hola mundo"
#Definimos la función:
def contar_frecuencias(cadena):
# Eliminamos los espacios y convertimos la cadena a minúsculas para unificar el conteo
    cadena = cadena.replace(" ", "").lower()
    frecuencias = {}
# Iteramos sobre cada letra en la cadena y contamos las apariciones
    for letra in cadena:
        frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias
#Hacemos un print para mostrar el conteo:
print(contar_frecuencias(cadena));

# Kata 2. Enunciado: Dada una lista de números, obtén una nueva lista con el doble de cada valor.
#Definimos lista de prueba:
lista = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#Definimos la función:
def duplicar_valores(lista):
# Se usa map() con una función lambda que multiplica cada elemento por 2
    return list(map(lambda x: x * 2, lista))
#Hacemos un print para mostrar la lista original y los valores resultantes tras la función
print(lista);
print(duplicar_valores(lista));

# Kata 3. Enunciado: Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
# Lista de prueba
lista_palabras = ["hola", "mundo", "python", "programación", "programador"]
palabra_objetivo = "pro"

# Función que filtra las palabras que contienen la palabra objetivo
def palabras_con_objetivo(lista_palabras, palabra_objetivo):
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# Llamamos a la función para imprimir el resultado por pantalla
resultado = palabras_con_objetivo(lista_palabras, palabra_objetivo)
print(f"Palabras que contienen '{palabra_objetivo}': {resultado}")

# Kata 4. Enunciado: Genera una función que calcule la diferencia entre los valores de dos listas.
lista1 = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
lista2 = [0, 2, 4, 6, 10, 16, 26, 42, 68, 110]
def diferencia_listas(lista1, lista2):
# Se usa map() con una función lambda que resta los elementos correspondientes de ambas listas
    return list(map(lambda x, y: x - y, lista1, lista2))
#Hacemos un print para mostrar el resultado de la diferencia entre listas
print(diferencia_listas(lista1, lista2));

# Kata 5. Enunciado: Escribe una función que tome una lista de números y un valor opcional (nota_aprobado, por defecto 5). La función debe calcular la media y devolver una tupla (media, "aprobado"/"suspenso").
#Definimos lista de prueba:
lista = [3, 6, 9, 7, 5]
#Definimos la función:
def estado_media(lista, nota_aprobado=5):
    if not lista:
        return (0, "suspenso")
    media = sum(lista) / len(lista)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)
#Hacemos un print para mostrar el resultado de la función
print(estado_media(lista));

# Kata 6. Enunciado: Escribe una función que calcule el factorial de un número de manera recursiva.
#Definimos la variable de ejemplo
n = 5
#Definimos la función:
def factorial(n):
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Llamada recursiva: n * factorial(n-1)
    return n * factorial(n - 1)
#Hacemos un print para mostrar el resultado de la función
print(factorial(n));
# Kata 7. Enunciado: Genera una función que convierta una lista de tuplas a una lista de strings.

#Definimos lista de prueba:
lista_tuplas = [(1,"dos"), (3, "cuatro"), (5, "seis")]
#Definimos la función:
def tuplas_a_strings(lista_tuplas):
    # Se usa map() para convertir cada tupla en una cadena concatenando sus elementos
    return list(map(lambda tupla: ''.join(map(str, tupla)), lista_tuplas))
#Hacemos un print para mostrar el resultado de la función
print(tuplas_a_strings(lista_tuplas));

# Kata 8. Enunciado: Escribe un programa que pida al usuario dos números e intente dividirlos. Maneja excepciones para entrada no numérica y división por cero.

#Definimos la función:
def dividir():
    try:
        # Preguntamos al usuario por el primer número
        num1 = float(input("Introduce el primer número: "))
        # Preguntamos al usuario por el segundo número
        num2 = float(input("Introduce el segundo número: "))
        # Realizamos la división
        resultado = num1 / num2
        # Mostramos el resultado
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    except ValueError:
        # Si se produce una excepción de tipo ValueError (entrada no numérica), mostramos un mensaje de error
        print("Error: Debes introducir números.")
    except ZeroDivisionError:
        # Si se produce una excepción de tipo ZeroDivisionError (división por cero), mostramos un mensaje de error
        print("Error: No se puede dividir por cero.")
# Llamamos a la función para que ejecute el programa
dividir();

# Kata 9. Enunciado: Escribe una función que tome una lista de nombres de mascotas y devuelva una nueva lista excluyendo las mascotas prohibidas ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].

#Definimos lista de prueba:
mascotas = ["Mapache","Perro", "Tigre", "Serpiente Pitón", "Gato", "Cocodrilo", "Canario", "Oso"]
#Definimos la función:  
def filtrar_mascotas_prohibidas(mascotas):  
    # Definimos la lista de mascotas prohibidas
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # Se usa una comprensión de lista para filtrar las mascotas que no están en la lista de prohibidas  
    return [mascota for mascota in mascotas if mascota not in mascotas_prohibidas]
#Hacemos un print para mostrar el resultado de la función
print(filtrar_mascotas_prohibidas(mascotas));

# Kata 10. Enunciado: Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada.

#Definimos lista de prueba:
lista_numeros = [1, 2, 3, 4, 5]
#Definimos la función:
def calcular_promedio(lista_numeros):
    if not lista_numeros:
        # Si la lista está vacía, lanzamos una excepción personalizada
        raise ValueError("La lista no puede estar vacía.")
    return sum(lista_numeros) / len(lista_numeros)
print(calcular_promedio(lista_numeros));

# Kata 11. Enunciado: Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
#Definimos la función:
def validar_edad():
    while True:  # Bucle para volver a pedir la edad en caso de error
        try:
            edad = int(input("Introduce tu edad: "))
            if edad < 0 or edad > 120:
                raise ValueError("La edad debe estar entre 0 y 120.")
            print(f"Edad válida: {edad}")
            return edad  # Solo retorna si la edad es válida
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

# Llamada a la función para probarla
validar_edad()

# Kata 12. Enunciado: Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra.

#Definimos la frase de prueba:
frase = "Hola mundo, desde Python"
#Definimos la función:
def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))
#Hacemos un print para mostrar el resultado de la función
print(longitud_palabras(frase));

# Kata 13. Enunciado: Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico.
#Definimos el conjunto de prueba:
caracteres = "Hola Mundo"
#Definimos la función:
def mayusculas_minusculas(caracteres):
    return list(set(map(lambda x: (x.upper(), x.lower()), caracteres))),
    print (mayusculas_minusculas(caracteres));
# Kata 14. Enunciado: Crea una función que retorne las palabras de una lista que comiencen con una letra en específico
#Definimos la lista de prueba:
lista_palabras = ["hola", "mundo", "python", "programación", "programador"]

# Definimos la letra de prueba: 
letra = "p"

# Definimos la función:
def palabras_letra(lista_palabras, letra):
    return [palabra for palabra in lista_palabras if palabra.startswith(letra)]
#Hacemos un print para mostrar el resultado de la función
print(palabras_letra(lista_palabras, letra));
# Kata 15. Enunciado: Crea una función lambda que sume 3 a cada número de una lista dada.
#Definimos la lista de prueba:
lista = [1, 2, 3, 4, 5]

# Definimos la función lambda:

suma_tres = lambda lista: list(map(lambda x: x + 3, lista))
#Hacemos un print para mostrar el resultado de la función
print(lista)
print(suma_tres(lista));

# Kata 16. Enunciado: Escribe una función que tome una lista de palabras y un entero n, y devuelva las palabras que tengan longitud mayor que n.
#Definimos la lista de prueba:
lista_palabras = ["hola", "mundo", "python", "programación", "programador"]
#Definimos la longitud de prueba:   
n = 5
#Definimos la función:
def palabras_longitud(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]
#Hacemos un print para mostrar el resultado de la función
print(palabras_longitud(lista_palabras, n));

# Kata 17. Enunciado: Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572)
#Definimos la lista de prueba:
digitos = [5,7,2]

# Definimos la función:
def numero_correspondiente(digitos):
    return int(''.join(map(str, digitos)))
#Hacemos un print para mostrar el resultado de la función
print(numero_correspondiente(digitos));

# Kata 18. Enunciado: Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.
#Definimos la lista de diccionario de prueba:
estudiantes = [
    {"nombre": "Juan", "edad": 20, "calificacion": 85},
    {"nombre": "Pedro", "edad": 21, "calificacion": 92},
    {"nombre": "Maria", "edad": 22, "calificacion": 88},
    {"nombre": "Ana", "edad": 23, "calificacion": 95}
]
#Definimos la función:
def calificacion_alta(estudiantes):
    return list(filter(lambda x: x["calificacion"] >= 90, estudiantes))
#Hacemos un print para mostrar el resultado de la función
print(calificacion_alta(estudiantes));
# Kata 19. Enunciado: Crea una función lambda que filtre los números impares de una lista.
#Definimos la lista de prueba:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Definimos la función lambda:
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
#Hacemos un print para mostrar el resultado de la función
print(lista)
print(filtrar_impares(lista));

# Kata 20. Enunciado: Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int.

#Definimos la lista de prueba:
lista = [1, "hola", 3.5, 4, [5, 6], {"clave": "valor"}]
#Definimos la función:
def valores_int(lista):
    return list(filter(lambda x: isinstance(x, int), lista))
#Hacemos un print para mostrar el resultado de la función
print(lista)
print(valores_int(lista));

# Kata 21. Enunciado: CCrea una función que calcule el cubo de un número dado mediante una función lambda
#Definimos la variable:
x = int(input("Introduce el número: "))
#Definimos la función lambda:
cubo = lambda x: x ** 3
#Hacemos un print para mostrar el resultado de la función
print("Resultado: ",cubo(x));

# Kata 22. Enunciado: Dada una lista numérica, obtén el producto total de los valores de dicha lista.
#Importamos la función reduce
from functools import reduce
#Definimos la lista de prueba:
lista = [1, 2, 3, 4, 5]
#Definimos la función: 
def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)
    # Hacemos un print para mostrar el resultado de la función
print(lista)
print(producto_total(lista));

# Kata 23: Enunciado: Concatena una lista de palabras.
#Importamos la función reduce
from functools import reduce
#Definimos la lista de prueba:
palabras = ["hola", "mundo", "python"]
#Definimos la función:
def concatenar_palabras(palabras):
    return reduce(lambda x, y: x + " " + y, palabras)
# Hacemos un print para mostrar el resultado de la función
print(palabras)
print(concatenar_palabras(palabras));

# Kata 24, Enunciado: Calcula la diferencia total en los valores de una lista.
#Importamos la función reduce
from functools import reduce
#Definimos la lista de prueba:
lista = [1, 2, 3, 4, 5]

# Definimos la función:
def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)
# Hacemos un print para mostrar el resultado de la función
print(lista)
print(diferencia_total(lista));

# Kata 25. Enunciado: Crea una función que cuente el número de caracteres en una cadena de texto dada.
#Definimos la cadena de prueba:
cadena = "Hola mundo"
#Definimos la función:
def contar_caracteres(cadena):
    return len(cadena)
    # Hacemos un print para mostrar el resultado de la función
print(cadena)
print(contar_caracteres(cadena));

# Kata 26. Enunciado: Crea una función lambda que calcule el resto de la división entre dos números dados.
#Definimos las variables de prueba:
x = 10
y = 3

# Definimos la función lambda:
resto = lambda x, y: x % y
# Hacemos un print para mostrar el resultado de la función
print(resto(x, y));

# Kata 27. Enunciado: Crea una función que calcule el promedio de una lista de números.
#Definimos la lista de prueba:
lista = [1, 2, 3, 4, 5]

# Definimos la función:
def promedio_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)
# Hacemos un print para mostrar el resultado de la función
print(lista)
print(promedio_lista(lista));
# Kata 28. Enunciado: Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
#Definimos la lista de prueba:
lista = [1, 2, 3, 4, 2, 5, 6]
#Definimos la función:
def primer_duplicado(lista):
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1:
            return lista[i]
# Hacemos un print para mostrar el resultado de la función  
print(lista)
print(primer_duplicado(lista));

# Kata 29. Enunciado: Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
#Definimos la variable de prueba:
variable = 1234567890
#Definimos la función:
def enmascarar_variable(variable):
    return "#" * (len(str(variable)) - 4) + str(variable)[-4:]
    # Hacemos un print para mostrar el resultado de la función
print(variable)
print(enmascarar_variable(variable));

# Kata 30. Enunciado: Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
#Definimos las palabras de prueba:
palabra1 = "Roma"
palabra2 = "Amor"

# Definimos la función:
def son_anagramas(palabra1, palabra2):
    #Usamos la función lower para que compare todas las palabras en minusculas
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
# Hacemos un print para mostrar el resultado de la función
print(palabra1, palabra2)
print(son_anagramas(palabra1, palabra2));
# Kata 31. Enunciado: Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
#Definimos la lista de prueba:
nombres = ["Juan", "Pedro", "Maria", "Ana"]
#Definimos la función:
def buscar_nombre(nombres):
    nombre = input("Introduce un nombre: ")
    if nombre in nombres:
        print(f"{nombre} está en la lista.")
    else:
        print(f"{nombre} no está en la lista.")
# Llamamos a la función para que ejecute el programa
buscar_nombre(nombres);

# Kata 32. Enunciado: Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
#Definimos la lista de prueba:
empleados = [
    {"nombre": "Juan", "puesto": "Gerente"},
    {"nombre": "Pedro", "puesto": "Desarrollador"},
    {"nombre": "Maria", "puesto": "Gerente"},
    {"nombre": "Ana", "puesto": "Analista"}
]   
nombre = input("Introduce un nombre: ")
print(nombre)
#Definimos la función:
def buscar_puesto(empleados, nombre):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return empleado["puesto"]
    return f"{nombre} no trabaja aquí."
# Hacemos un print para mostrar el resultado de la función
print("Puesto:", buscar_puesto(empleados, nombre))

# Kata 33. Enunciado: Crea una función lambda que sume elementos correspondientes de dos listas dadas.
#Definimos las listas de prueba:
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Definimos la función lambda:
sumar_listas = lambda lista1, lista2: [x + y for x, y in zip(lista1, lista2)]

# Hacemos un print para mostrar el resultado de la función
print(lista1, lista2)
print(sumar_listas(lista1, lista2));

# Kata 34. Enunciado: Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
#Definimos la clase Arbol:
class Arbol:
    def __init__(self, nombre):
        #Inicializamos el arbolo con un nombre y un tronco de longitud 1
        self.nombre = nombre
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # Incrementa en una unidad la longitud del tronco.
        self.tronco += 1

    def nueva_rama(self):
        # Añade una nueva rama al árbol con longitud 1.
        self.ramas.append(1)

    def crecer_ramas(self):
        # Incrementa en una unidad la longitud de todas las ramas del árbol.
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # Retira la rama situada en la posición dada (índice) si existe.
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
            print(f"Rama en posición {posicion} eliminada.")
        else:
            print(f"No existe una rama en la posición {posicion}.")

    def info_arbol(self):
        # Muestra la información del árbol: nombre, longitud del tronco, número de ramas y longitudes de las ramas.
        print("\nInformación del Árbol")
        print(f"Nombre: {self.nombre}")
        print(f"Longitud del tronco: {self.tronco}")
        print(f"Número de ramas: {len(self.ramas)}")
        print(f"Longitudes de las ramas: {self.ramas}")
        print("------------------------------")


def mostrar_menu():
    # Muestra el menú de opciones disponibles aplicando los casos de uso del enunciado.
    print("\nMenú:")
    print("1. Crear árbol")
    print("2. Hacer crecer el tronco una unidad")
    print("3. Añadir una nueva rama al árbol")
    print("4. Hacer crecer todas las ramas del árbol")
    print("5. Añadir dos nuevas ramas al árbol")
    print("6. Retirar la rama situada en la posición 2")
    print("7. Obtener información del árbol")
    print("8. Salir")


def main():
    arbol = None  # No hay árbol al iniciar

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            nombre = input("Introduce el nombre o especie del árbol: ")
            arbol = Arbol(nombre)
            print(f"Árbol '{nombre}' creado con éxito.")

        elif opcion == "2":
            if arbol:
                arbol.crecer_tronco()
                print("El tronco ha crecido en una unidad.")
            else:
                print("Primero debes crear un árbol (opción 1).")

        elif opcion == "3":
            if arbol:
                arbol.nueva_rama()
                print("Se ha añadido una nueva rama.")
            else:
                print("Primero debes crear un árbol (opción 1).")

        elif opcion == "4":
            if arbol:
                arbol.crecer_ramas()
                print("Todas las ramas han crecido en una unidad.")
            else:
                print("Primero debes crear un árbol (opción 1).")

        elif opcion == "5":
            if arbol:
                arbol.nueva_rama()
                arbol.nueva_rama()
                print("Se han añadido dos nuevas ramas.")
            else:
                print("Primero debes crear un árbol (opción 1).")

        elif opcion == "6":
            if arbol:
                arbol.quitar_rama(2)
            else:
                print("Primero debes crear un árbol (opción 1).")

        elif opcion == "7":
            if arbol:
                arbol.info_arbol()
            else:
                print("Primero debes crear un árbol (opción 1).")

        elif opcion == "8":
            print("Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()

# Kata 36. Enunciado: Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#Definimos la clase UsuarioBanco:
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        # Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, monto):
        #Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
        if monto > self.saldo:
            raise ValueError(f"Saldo insuficiente en {self.nombre}. No se puede retirar {monto}.")
        self.saldo -= monto
        print(f"{self.nombre} ha retirado {monto}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, monto):
        #Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
        if monto > self.saldo:
            raise ValueError(f"Saldo insuficiente en {self.nombre} para transferir {monto}.")
        self.saldo -= monto
        otro_usuario.saldo += monto
        print(f"{self.nombre} ha transferido {monto} a {otro_usuario.nombre}.")
        print(f"Saldo de {self.nombre}: {self.saldo}, Saldo de {otro_usuario.nombre}: {otro_usuario.saldo}")

    def agregar_dinero(self, monto):
        #Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
        self.saldo += monto
        print(f"{self.nombre} ha agregado {monto}. Saldo actual: {self.saldo}")


# Caso de uso
if __name__ == "__main__":
    #1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    #2. Agregar 20 unidades de saldo de "Bob".
    try:
        bob.agregar_dinero(20)
    except Exception as e:
        print(f"Error al agregar dinero a {bob.nombre}: {e}")

    #3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
    try:
        bob.transferir_dinero(alicia, 80)
    except Exception as e:
        print(f"Error en la transferencia de {bob.nombre} a {alicia.nombre}: {e}")

    # 4. Retirar 50 unidades de saldo a "Alicia".
    try:
        alicia.retirar_dinero(50)
    except Exception as e:
        print(f"Error al retirar dinero de {alicia.nombre}: {e}")

    # Mostrar saldos finales de ambos usuarios.
    print(f"\nSaldo final de {alicia.nombre}: {alicia.saldo}")
    print(f"Saldo final de {bob.nombre}: {bob.saldo}")

# Kata 37. Enunciado: Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .

#1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
def contar_palabras(texto):
    palabras = texto.lower().split()
    return {palabra: palabras.count(palabra) for palabra in set(palabras)}

#2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
def reemplazar_palabras(texto, palabra_objetivo, reemplazo):
    palabras = texto.split()
    resultado = [
        reemplazo if palabra.lower() == palabra_objetivo.lower() else palabra
        for palabra in palabras
    ]
    return " ".join(resultado)

#3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
def eliminar_palabras(texto, palabra_objetivo):
    palabras = texto.split()
    # Separamos el texto en palabras y reconstruimos la cadena omitiendo las coincidencias.
    resultado = [palabra for palabra in palabras if palabra.lower() != palabra_objetivo.lower()]
    return " ".join(resultado)

#4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        resultado = contar_palabras(texto)
        print("Frecuencia de palabras (ignorando mayúsculas):")
        for palabra, cantidad in resultado.items():
            print(f"'{palabra}': {cantidad}")
        return texto

    elif opcion == "reemplazar":
        if len(args) < 2:
            print("Faltan argumentos para reemplazar.")
            return texto
        palabra, reemplazo = args
        return reemplazar_palabras(texto, palabra, reemplazo)

    elif opcion == "eliminar":
        if len(args) < 1:
            print("Falta la palabra a eliminar.")
            return texto
        palabra = args[0]
        return eliminar_palabras(texto, palabra)

    else:
        print("Opción no válida.")
        return texto

#Seleccionamos los casos de uso mediante el menú interactivo.
def mostrar_menu():
    print("\nOpciones:")
    print("1. Contar palabras")
    print("2. Reemplazar palabras")
    print("3. Eliminar palabras")
    print("4. Salir")

def main():
    texto = input("Introduce el texto: ")

    while True:
        print("\nTexto actual:")
        print(texto)
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            texto = procesar_texto(texto, "contar")

        elif opcion == "2":
            palabra = input("Introduce la palabra a reemplazar: ")
            reemplazo = input("Introduce la nueva palabra: ")
            texto = procesar_texto(texto, "reemplazar", palabra, reemplazo)

        elif opcion == "3":
            palabra = input("Introduce la palabra a eliminar: ")
            texto = procesar_texto(texto, "eliminar", palabra)

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

        print("\nTexto resultante:")
        print(texto)

if __name__ == "__main__":
    main()

# Kata 38. Enunciado: 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def periodo_dia(hora_decimal):
    #Definimos los parametros para trabajar con la variable float hora_decimal, para poder hacer calculos
    if 6 <= hora_decimal < 12:
        return "Es de día"
    elif 12 <= hora_decimal < 18:
        return "Es de tarde"
    elif 0 <= hora_decimal < 6 or 18 <= hora_decimal < 24:
        return "Es de noche"
    else:
        raise ValueError("La hora debe estar entre 0:00 y 23:59.")


def hora_usuario():
    #Solicitamos el input de la hora al usuario en formato HH:MM
    while True:
        entrada = input("Introduce la hora en formato HH:MM (ej. 14:30): ")
        try:
            partes = entrada.strip().split(":")
            if len(partes) != 2:
                raise ValueError("Formato incorrecto. Usa HH:MM.")

            hora = int(partes[0])
            minutos = int(partes[1])

            if not (0 <= hora <= 23) or not (0 <= minutos <= 59):
                raise ValueError("Hora o minutos fuera de rango.")

            # Convertimos a formato decimal
            hora_decimal = hora + minutos / 60
            return hora_decimal

        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")


def main():
    hora_decimal = hora_usuario()
    periodo = periodo_dia(hora_decimal)
    print(f"\n{periodo}")


if __name__ == "__main__":
    main()

# Kata 39. Enunciado: Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son: 0 - 69 Insuficiente, 70 - 79 Bien, 80 - 89 Muy Bien, 90 - 100 Excelente.
def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy Bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        raise ValueError("La nota debe estar entre 0 y 100.")


def main():
    while True:
        entrada = input("Introduce la nota (0-100): ")
        try:
            nota = int(entrada)
            if nota < 0 or nota > 100:
                raise ValueError("Rango fuera de lo permitido.")
            calificacion = calificacion_texto(nota)
            print(f"Nota introducida: {nota}, calificación: {calificacion}")
            break  # Salimos del bucle si la nota fue válida
        except ValueError as e:
            print(f"Error: {e}. Intenta nuevamente.")


if __name__ == "__main__":
    main()

# Kata 40. Enunciado: Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcular_area(figura, datos):

    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        (radio,) = datos
        return 3.1416 * (radio ** 2)
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no reconocida.")

def main():
    print("Calculadora de áreas")

    while True:
        figura = input("Introduce el tipo de figura: ").strip().lower()

        if figura not in {"rectangulo", "triangulo", "circulo"}:
            print("Tipo de figura no válido. Intenta con: rectangulo, triangulo o circulo.")
            continue

        try:
            if figura == "rectangulo" or figura == "triangulo":
                base = float(input("Introduce la base: "))
                altura = float(input("Introduce la altura: "))
                datos = (base, altura)
            elif figura == "circulo":
                radio = float(input("Introduce el radio: "))
                datos = (radio,)
            
            area = calcular_area(figura, datos)
            print(f"El área del {figura} es: {area:.2f}")
            break  # Finaliza después de un cálculo exitoso

        except ValueError as e:
            print("Error: {e}. Asegúrate de introducir s válidos.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()

#Kata 41. Enunciado: En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
def calcular_precio_final():
    print("Bienvenido a la tienda en línea")

    while True:
        try:
            # 1. Solicita al usuario que ingrese el precio original de un artículo.
            precio_original = float(input("\nIntroduce el precio original del artículo (€): "))

            if precio_original <= 0:
                print("El precio debe ser mayor que cero.")
                continue

            # 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
            tiene_cupon = input("¿Tienes un cupón de descuento? (Si/No): ").strip().lower()
            #3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
            if tiene_cupon == "si":
                try:
                    descuento = float(input("Introduce el valor del cupón (€): "))
                    #4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
                    if descuento <= 0:
                        print("El valor del cupón debe ser mayor que cero.")
                        continue
                    elif descuento > precio_original:
                        print("El valor del cupón no puede ser mayor que el precio del artículo.")
                        print("Vuelve a introducir un nuevo precio.")
                        continue
                    elif descuento == precio_original:
                        print("El cupón cubre el total del precio. El artículo te saldrá gratis.")
                        precio_final = 0
                    else:
                        precio_final = precio_original - descuento

                except ValueError:
                    print("Valor del cupón no válido. Inténtalo nuevamente.")
                    continue

            elif tiene_cupon == "no":
                precio_final = precio_original

            else:
                print("Respuesta inválida. Se asumirá que no tienes cupón.")
                precio_final = precio_original

            # 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
            print(f"\nEl precio final de la compra es: {precio_final:.2f}€")
            break  # Finalizamos si todo ha salido correctamente

        except ValueError:
            print("Entrada no válida. Asegúrate de introducir números correctos.")


if __name__ == "__main__":
    calcular_precio_final()