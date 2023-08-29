#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
valores = list(map(int, input().split()))
arbol = []
for valor in valores:
    if arbol == []:
        arbol = [valor, [], [], []]
    else:
        nodo = arbol
        while True:
            if valor < nodo[0]:
                if nodo[1] == []:
                    nodo[1] = [valor, [], [], []]
                    break
                else:
                    nodo = nodo[1]
            elif valor > nodo[0]:
                if nodo[3] == []:
                    nodo[3] = [valor, [], [], []]
                    break
                else:
                    nodo = nodo[3]
            else:
                if nodo[2] == []:
                    nodo[2] = [valor, [], [], []]
                    break
                else:
                    nodo = nodo[2]
print(arbol)

