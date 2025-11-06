Numero = 10

#
Numero += 1
print(Numero)

#Concatenar con +
Nombre = "Pedro"
Bienvenida = "bienvenido al hotel " + Nombre + " Como puedo ayudarle?"
print(Bienvenida)

#Concatenar con f-strings
Bienvenida = f"bienvenido al hotel {Numero} Como puedo ayudarle?"
print(Bienvenida)

#Operadores de Pertenencia
print("bienvenido" in Bienvenida)
print("bienvenido" not in Bienvenida)