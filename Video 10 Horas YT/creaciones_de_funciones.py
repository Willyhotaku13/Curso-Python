#Crear una funcion simple:
#def saludar():
    #print("Hola Master!")

#Ejecutando la funcion simple
#saludar()

#Crear una funcion con parametros:
#Las variable en la linea de creacion de la funcion son variables que solo funcionan dentro de la funcion y necesitan que se les de un valor cuando de llame la funcion.
#Si creas las variables dentro de la funcion en si no es necesario darle los valores cuando se llama la funcion.
def saludar(nombre,genero):

    if genero == "mujer":
        adjetivo = "reina"

    elif genero == "hombre":
        adjetivo = "master"

    else :
        adjetivo = "clanker"

    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?")

#Llamando la funcion y dandole los datos a las variables "nombre" y "genero"
saludar("Weeb","mujer")
