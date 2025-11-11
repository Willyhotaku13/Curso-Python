#Pedirle un dato al usuario
nombre = input("Ingresa tu nombre: ") #input siempre devuelve un string aunque le ingreses un numero.
print(f"Tu nombre es: {nombre} " + "Waos")

num_1_string = input("ingresa un numero: ")
num_1_int = int(num_1_string) #convertimos el texto ingresado en un numero, tambien se puede usar float(num_1_string).
print(type(num_1_int)) #verificamos que tipo de dato es ahora


