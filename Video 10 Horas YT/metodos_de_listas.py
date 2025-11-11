lista = ["Hola","Mundo",67,True]

#Devuelve la cantidad de elementos, en este caso de una lista, si fuera solo un string devuelve la cantidad de caracteres.
cantidad = len(lista)
print(cantidad)

#Agregar un elemento a la lista con append (no es necesario guardar el resultado en una variable, solo ejecutar el metodo)
#lista_append = lista.append("LOOOL") no es necesario hacerlo asi.
lista.append("LOOOL")
print(lista)

#Agregar un elemento a la lista en un indice especifico
lista.insert(2,"Elemento agregado")
print(lista)

#Agregar varios elementos a la lista, se agrega una lista dentro de otra.
lista.extend([False,2025])
print(lista)

#Eliminar un elemento de la lista, se tiene que indicar el indice
lista.pop(2) #-1 para eliminar el ultimo de la lista, -2 para el anteultimo y asi sucesivamente.

#Eliminar un elemento de la lista por su valor
lista.remove("Mundo") #Si no encuentra el elemento manda un error (excepcion)

#Eliminar todos los elementos de la lista
#lista.clear()

#Ordenar los elementos de una lista de forma ascendente (No funciona si tiene strings, solo con numeros y booleanos)
lista_2 = [13,10,5,0,1,7]
lista_2.sort() #Si le agregamos el parametro reverse=True lo ordena en reversa
lista_2.sort(reverse=True)
print(lista_2)

#Invertir los elementos de una lista, no es igual que .sort(reverse=True) ya que .reverse() no ordena los elementos, solo los inverte. Por eso puede funcionar con strings.
lista.reverse()
print(lista)

#Verificar si un elemento se encuentra en la lista, si aparece nos devuelve su indice.
elemento_encontrado = lista.index(67)
print(elemento_encontrado)