cadena_1 = "Hello World"
cadena_2 = "Bienvenido Master"
cadena_3 = "Hello,World,Bienvenido,Master"

#Los metodos tienen la siguiente estructura: dato.metodo()
prueba = cadena_1.upper()
print(prueba)

#Verificar los metodos disponibles para un tipo de dato o variable(varian segun el tipo de dato):
print(dir(cadena_2))

#Sirve para buscar valores en una cadena y nos devuelve su indice de posicion, si no lo encuentra devuelve -1
prueba_find = cadena_2.find("i")
print(prueba_find)

#Sirve para buscar valores en una cadena y nos devuelve su indice de posicion, si no lo encuentra marca un error (una exepcion).
prueba_index = cadena_2.find("i")
print(prueba_index)

#Sirve para buscar valores en una cadena, devuelve la cantidad de veces que aparece el parametro que le indicamos
contar_coincidencias = cadena_2.count("e")
print(contar_coincidencias)

#Contar cuantos caracteres tiene una cadena. (es una funcion, no un metodo, las funciones tiene esta estructura: funcion(valor o variable))
cantidad_caracteres = len(cadena_2)
print(cantidad_caracteres)

#si el valor 1 se encuentra lo cambia por el valor 2.
cadeda_reemplazada = cadena_2.replace("Bien", "Mal")
print(cadeda_reemplazada)

#separa una cadena y la convierte en lista segun el parametro que le indiquemos, en este caso una coma (",")
cadena_listada = cadena_3.split(",")
print(type(cadena_listada))
print(cadena_listada)
