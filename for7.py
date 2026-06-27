a = [4, 9, 2, 9, 5, 9, 7]

primera = 0
ultima= 0
numero = 9
apariciones = 0
for i in range(7):
    if a[i] == numero:
        apariciones += 1
        if apariciones == 1:
            primera = i
        ultima = i
print(numero, "tiene primera aparición: posición", primera, "ultima: posición", ultima,"apariciones totales", apariciones)
