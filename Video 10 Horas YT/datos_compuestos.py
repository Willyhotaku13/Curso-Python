#lista
lista_de_compras_1 = ["Limpia Platos","Fundas De Basura","Jamon","Ketchup",True,1.60]
print(lista_de_compras_1)
print(lista_de_compras_1[0])

#tupla (lista no modificable despues de ser declarado su valor)
lista_de_compras_2 = ("Limpia Platos","Fundas De Basura","Jamon","Ketchup",True,1.60)

#cambiamos un valor de la lista
lista_de_compras_1[4] = False
print(lista_de_compras_1)

#intentamos cambiar un valor de la tupla, no se puede.
#lista_de_compras_2[4] = False
#print(lista_de_compras_2)

#Crear Un Conjunto (set), No se pueden llamar los elemtos por su indice. No muestra duplicados. 
conjunto = {"Limpia Platos","Fundas De Basura","Jamon","Ketchup",True,1.60}
print(conjunto)

#Diccionarios, parecido a una lista simple, solo que se busca por nombre asociado
diccionario = {
    "Nombre": "Willy",
    "Edad": 23,
    "Souls_Bro": True,
    "Duplicado": 23
}

print(diccionario["Nombre"])

