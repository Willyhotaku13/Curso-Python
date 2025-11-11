diccionario_1 = {
"Nombre" : "Weeb",
"Apellido" : "Bruh",
"Año" : 2002
}

#Este medoto devuelve las claves/indices del diccionario.(Tambien sirve para interar)
claves = diccionario_1.keys()
print(claves)

#Buscar un valor por su clave/indice en un diccionario
#claves = diccionario_1.get("Año") se puede guardar en una variable o imprimir el metodo sin guardarlo como en la mayoria de metodos.
print(diccionario_1.get("Año"))

#Eliminar todo el diccionario
#diccionario_1.clear()
print(diccionario_1)

#Eliminar un elemento del diccionario
diccionario_1.pop("Apellido")
print(diccionario_1)

#Obtener un elemento dict_items iterable
diccionario_1_iterable = diccionario_1.items()
print(diccionario_1_iterable)