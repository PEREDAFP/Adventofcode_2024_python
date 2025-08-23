def resolver( parte: int, iterador ):
    sopa_letras= []
    for linea in iterador:
        sopa_letras.append(linea)
    filas = len(sopa_letras)
    columnas = len(sopa_letras[0])
    if parte == 1:
        #Tenemos que encontrar, en una sopa de letras, todas las XMAS posibles
        #Hay que tener en cuenta que pueden estar de arriba a abajo, de izquierda a derecha, en diagonal....    
        direcciones = [
            (0, 1),   # derecha
            (0, -1),  # izquierda
            (1, 0),   # abajo
            (-1, 0),  # arriba
            (1, 1),   # abajo-derecha
            (1, -1),  # abajo-izquierda
            (-1, 1),  # arriba-derecha
            (-1, -1)  # arriba-izquierda
        ]
        
        contador = 0
        for i in range(filas):
            for j in range(columnas):
                for dr, dc in direcciones:
                    end_i = i + 3 * dr
                    end_j = j + 3 * dc
                    if end_i < 0 or end_i >= filas or end_j < 0 or end_j >= columnas:
                        continue
                    if sopa_letras[i][j] == 'X' and sopa_letras[i+dr][j+dc] == 'M' and sopa_letras[i+2*dr][j+2*dc] == 'A' and sopa_letras[i+3*dr][j+3*dc] == 'S':
                        contador += 1
        
        print(f"El resultado de día 4 parte 1 es {contador}")    
    
    elif parte == 2:
        contador = 0
        for i in range(1, filas-1):
            for j in range(1, columnas-1):
                if sopa_letras[i][j] == 'A':
                    
                    if sopa_letras[i-1][j-1] == 'M' and sopa_letras[i-1][j+1] == 'S' and sopa_letras[i+1][j-1] == 'M' and sopa_letras[i+1][j+1] == 'S':
                        contador += 1
                
                    elif sopa_letras[i-1][j-1] == 'S' and sopa_letras[i-1][j+1] == 'M' and sopa_letras[i+1][j-1] == 'S' and sopa_letras[i+1][j+1] == 'M':
                        contador += 1

                    elif sopa_letras[i-1][j-1] == 'S' and sopa_letras[i-1][j+1] == 'S' and sopa_letras[i+1][j-1] == 'M' and sopa_letras[i+1][j+1] == 'M':
                        contador += 1
                    elif sopa_letras[i-1][j-1] == 'M' and sopa_letras[i-1][j+1] == 'M' and sopa_letras[i+1][j-1] == 'S' and sopa_letras[i+1][j+1] == 'S':
                        contador += 1
       
        print(f"El resultado de día 4 parte 2 es {contador}")
    else:
        print("No existe esa parte")

    