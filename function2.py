a = [8, 3, 15, 6, 1]

def encontrar_mayor(lista):
    mayor = 0
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

elmayor = encontrar_mayor(a)
print("el numero mayor de la lista *a* es:", elmayor)
print("---------------------")

def encontrar_menor(lista):
    menor = 99999
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

elmenor = encontrar_menor(a)
print("el numero menor de la lista *a* es:", elmenor)
print("---------------------")
def diferencia(mayor, menor):
        diferencianum = mayor - menor
        return diferencianum

ladiferencia = diferencia(encontrar_mayor(a), encontrar_menor(a))
print("la diferencia de los números mayor y menor es de:", ladiferencia)