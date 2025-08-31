def contar_pasos_1(mapa):
    OBSTACULO = '#'
    filas = len(mapa)
    columnas = len(mapa[0])
    visitadas = []
   
    # Direcciones: arriba, derecha, abajo, izquierda
    direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    simbolos = {'^': 0, '>': 1, 'v': 2, '<': 3}

    # Encontrar posición inicial y dirección
    x, y, dir_idx = next(
        ( (i, j, simbolos[mapa[i][j]]) 
        for i in range(filas) 
        for j in range(columnas) 
        if mapa[i][j] in simbolos ),
        (None, None, None)  # valor por defecto si no encuentra nada
    )
    pasos = 0

    while True:
        #Incrementamos x e y con la dirección obtenidoa
        dx, dy = direcciones[dir_idx]
        nx, ny = x + dx, y + dy

        # Caso de salida del mapa
        if not (0 <= nx < filas and 0 <= ny < columnas):
            return pasos  # termina
           
        # Caso obstáculo
        if mapa[nx][ny] == OBSTACULO:
            dir_idx = (dir_idx + 1) % 4  # girar derecha         
        else:
            x, y = nx, ny
            if not ((x,y) in visitadas):
                pasos += 1
                visitadas.append((x,y))
           


def resolver( parte: int, iterador ):
    mapa = []
    for linea in iterador:
        mapa.append(linea)

    if parte == 1:     
        print(f"El resultado de día 6 parte 1 es {contar_pasos_1(mapa)}")  
  
    elif parte == 2:       
        print(f"El resultado de día 5 parte 2 es ")
    else:
        print("No existe esa parte")

    