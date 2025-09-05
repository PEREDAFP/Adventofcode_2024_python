
OBSTACULO = '#'

# Direcciones: arriba, derecha, abajo, izquierda    
DIRECCIONES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
SIMBOLOS = {'^': 0, '>': 1, 'v': 2, '<': 3}

def contar_pasos_1(mapa):
    
    filas = len(mapa)
    columnas = len(mapa[0])
    visitadas = []
   

    # Encontrar posición inicial y dirección
    x, y, dir_idx = next(
        ( (i, j, SIMBOLOS[mapa[i][j]]) 
        for i in range(filas) 
        for j in range(columnas) 
        if mapa[i][j] in SIMBOLOS ),
        (None, None, None)  # valor por defecto si no encuentra nada
    )
    pasos = 0

    while True:
        #Incrementamos x e y con la dirección obtenidoa
        dx, dy = DIRECCIONES[dir_idx]
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
           
def comprobando_bucle(mapa):
    #Voy creando el recorrido.
    #Si me encuentro al final del mapa devolveré False porque no hay bucle
    #Si me encuentro dos veces en la misma posición y dirección será un bucle y saldré con True
    # Voy a utilizar un set para visitadas
    filas = len(mapa)
    columnas = len(mapa[0])
    visitadas = set()
   
    
    # Encontrar posición inicial y dirección
    x, y, dir_idx = next(
        ( (i, j, SIMBOLOS[mapa[i][j]]) 
        for i in range(filas) 
        for j in range(columnas) 
        if mapa[i][j] in SIMBOLOS ),
        (None, None, None)  # valor por defecto si no encuentra nada
    )
    if x == None: return False #Hemos pasado un mapa sin inicio, problablemente al sobreescribir esa casilla con un obstáculo 
    #Añadimos en visitada la primera posición
    visitadas.add((x,y, dir_idx))
    while True:
        #Incrementamos x e y con la dirección obtenidoa
        dx, dy = DIRECCIONES[dir_idx]
        nx, ny = x + dx, y + dy

        # Caso de salida del mapa
        if not (0 <= nx < filas and 0 <= ny < columnas): return False # No hemos encontrado ningún bucle ytermina
           
        # Caso obstáculo
        if mapa[nx][ny] == OBSTACULO:
            dir_idx = (dir_idx + 1) % 4  # girar derecha         
        else:
            x, y = nx, ny
            #Creamos un array con la posición x e y, la dirección que tiene en ese momento y el índice de dicha posición
            #Lo del índice hay que mirarlo, pero creo que facilitará los cálculos en el siguiente paso
            if (x,y, dir_idx) in visitadas:
                return True #Hemos encontrado un bucle ya que hemos vuelto a la misma posición con la misma dirección
            #Añadimos la casilla y la dirección a visitadas       
            visitadas.add((x,y,dir_idx))

def contamos_bucles(mapa):
    #Vamos a ir añadiendo obstáculos nuevos al mapa y comprobamos si ese mapa nuevo contiene un bucle
    #Si se produce un bucle lo contamos
    bucles = 0
    filas = len(mapa)
    columnas = len(mapa[0])

    for y in range(filas):
        for x in range(columnas):
            #Vamos a añadir un nuevo obstáculo
            # Como estamos trabajando con cadenas de caracteres lo hacemos con la función reemplazar
            #Creamos una copia de mapa para mantener las posiciones que no forman parte de 
            mapa_cop = mapa.copy()
            mapa_cop[y] = reemplazar(mapa_cop[y], x, OBSTACULO)
            bucles += int(comprobando_bucle(mapa_cop))

    return bucles 



def reemplazar(cadena, pos, char):
    """
    Devuelve una nueva cadena con el carácter en la posición `pos` reemplazado por `char`.
    """
    if pos < 0 or pos >= len(cadena):
        raise IndexError("Posición fuera de rango")
    if len(char) != 1:
        raise ValueError("Solo se puede reemplazar por un único carácter")

    return cadena[:pos] + char + cadena[pos+1:]





def resolver( parte: int, iterador ):
    mapa = []
    for linea in iterador:
        mapa.append(linea)

    if parte == 1:     
        print(f"El resultado de día 6 parte 1 es {contar_pasos_1(mapa)}")  
  
    elif parte == 2: 
        print(f"El resultado de día 5 parte 2 es {contamos_bucles(mapa)} ")
        
    else:
        print("No existe esa parte")

    