# 1. Escribir una función que calcule el máximo común divisor entre dos números.
def max_common_divisor(a,b):
    while b:
        a, b = b, a % b
    return a

a = 24
b = 36

print(max_common_divisor(a, b))

# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def min_common_multiple(a, b):
    max_divisor = max_common_divisor(a, b)
    min_multiple = (a * b) // max_divisor
    return min_multiple

a = 24
b = 36

print(min_common_multiple(a, b))

# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
def count_words(string):
    words = string.lower().split() # Split the string into words and convert to lowercase
    word_counts = {} # Create an empty dictionary to store the word counts
    for word in words: # Loop over the words and count the frequency of each word
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

input_string = "The quick brown fox jumps over the lazy dog"
word_counts = count_words(input_string)
print(word_counts)

# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). 
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
def most_frequent_word(word_counts):
    most_frequent = None # Initialize variables to store the most frequent word and its count
    highest_count = 0
    for word, count in word_counts.items(): # Loop over the dictionary and update the most frequent word and its count
        if count > highest_count:
            most_frequent = word
            highest_count = count
    return (most_frequent, highest_count)

most_frequent = most_frequent_word(word_counts)
print(most_frequent)

# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() 
# que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.
def get_init():
    while True:
        try:
            num = int(input('Please enter an integer: '))
            return num
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

num = get_init()
print('The entered number is: ', num)

# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# - mostrar(): Muestra los datos de la persona.
# - Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
class Persona:
    def __init__(self, nombre = '', edad = 0, dni = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        check = isinstance(valor, str)
        if check:
            self.__nombre = valor
        else:
            print("Error: Name must be a string.")

    @property        
    def edad(self):
        return self.__edad

    @edad.setter    
    def edad(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self.__edad = valor
        else:
            print("Error: Age must be a non-negative integer.")

    @property        
    def dni(self):
        return self.__dni

    @dni.setter    
    def dni(self, valor):
        if isinstance(valor, int):
            self.__dni = valor
        else:
            print("Error: DNI must be a number.")
    
    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)
        
    def es_mayor_de_edad(self):
        return self.__edad >= 18

p1 = Persona()
p1.nombre = 'Juan Gomez' 
p1.edad = 25
p1.dni = 12345678
p1.mostrar()
print("Is", p1.nombre, "of legal age? ", p1.es_mayor_de_edad())

# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
# Crear los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos. 
# - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
# - mostrar(): Muestra los datos de la cuenta. 
# - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
# - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class Cuenta:
    def __init__(self, titular=None, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        if isinstance(valor, Persona):
            self.__titular = valor
        else:
            print("Error: Titular must be a Persona object.")

    @property
    def cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular:", self.__titular.nombre)
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


# Ejemplo de uso:
p2 = Persona("Maria Lopez", 30, 98765432)
c1 = Cuenta(p2, 1000.0)
c1.mostrar()

c1.ingresar(500.0)
c1.mostrar()

c1.retirar(2000.0)
c1.mostrar()

c1.retirar(500.0)
c1.mostrar()

# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7.
# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
# Crear los siguientes métodos para la clase:
# - Un constructor. 
# - Los setters y getters para el nuevo atributo. 
# - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el 
# titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
# - Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad = 0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, valor):
        if isinstance(valor, int) or isinstance(valor, float):
            self.__bonificacion = valor
        else:
            print("Error: La bonificación debe ser un número.")

    def es_titular_valido(self):
        if self.titular.es_mayor_de_edad() and self.titular.edad < 25:
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Error: No se puede retirar dinero de la cuenta.")

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.bonificacion, "%")


titular = Persona(nombre="Juan", edad=20, dni=12345678)
cuenta_joven = CuentaJoven(titular = titular, cantidad = 1000, bonificacion = 5)

if cuenta_joven.es_titular_valido():
    print("El titular de la cuenta joven es válido")
else:
    print("El titular de la cuenta joven no es válido")

cuenta_joven.mostrar()

cuenta_joven.ingresar(500)

cuenta_joven.retirar(2000)

cuenta_joven.mostrar()