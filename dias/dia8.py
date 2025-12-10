from itertools import combinations
#TODO: cambiar el combinations por código sin esta librería itertools

def comparar_todas(lista, limite):
    resultado = []

    # Recorrer todas las combinaciones posibles de 2 puntos
    for (x, y), (z, t) in combinations(lista, 2):

        # Primer punto: (2x - z, 2y - t)
        p1 = (2 * x - z, 2 * y - t)

        # Segundo punto: (2z - x, 2t - y)
        p2 = (2 * z - x, 2 * t - y)

        # Validar y agregar
        for px, py in (p1, p2):
            if 0 <= px < limite and 0 <= py < limite:
                resultado.append((px, py))

    return resultado



def resolver( parte: int, iterador ):

    matriz = []
    for linea in iterador:
            matriz.append(linea)
           
    if parte == 1:
        #Vamos a crear un diccionario con las letras y las posiciones que estas ocupan en la matriz
        diccionario = {}
        for fila_idx, fila in enumerate(matriz):
            for col_idx, caracter in enumerate(fila):
                if caracter != '.':
                    if caracter not in diccionario:
                        diccionario[caracter] = []
                    diccionario[caracter].append((fila_idx, col_idx))
        lista_fin = []
        for i in diccionario.keys():
            lista_fin.extend(comparar_todas(diccionario[i], len(matriz[0])))
        #Eliminamos los duplicados
        lista_fin = set(lista_fin)

        print(f"El resultado de día 8 parte 1 es {len(lista_fin)}")    
    elif parte == 2:
        print(f"El resultado de día 8 parte 2 es ")
    else:
        print("No existe esa parte")

    