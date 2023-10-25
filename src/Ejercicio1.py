def burbuja(lista):
    n = len(lista)
    intercambio = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1]:
                intercambio = True
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
         
        if not intercambio:
            return lista
        

if __name__ == "__main__":
    #Entrada
    lista = [8, 3, 1, 19, 14]
    #Proceso
    burbuja(lista)
    #Salida
    for i in range(len(lista)):
        print("% d" % lista[i], end=" ")
