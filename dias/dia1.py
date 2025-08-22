def resolver( parte: int, iterador ):
    
    lista1=[]
    lista2=[]
    for linea in iterador:
            aux = [ int(x) for x in  linea.split("  ") ]
            lista1.append(aux[0])
            lista2.append(aux[1])
        
    if parte == 1:
        #Tenemos que obtener la diferencia entre las columnas 1 y 2 haciendo la direrencia
        #entre el más pequeño de la lista2 menos el más pequeño de la lista 1, el segundo más pequeño de la
        #lista2 menos el segundo más pequeño de la lista1..
        lista1.sort()
        lista2.sort()
        print(f"El resultado de día 1 parte 1 es {sum (b-a for a, b in zip(lista1, lista2))}")    
    elif parte == 2:
        #Ahora tenemos que sumar cada número de la izquierda multiplicándolo por tantas veces como aparece en la derecha
        print(f"El resultado de día 1 parte 2 es {sum (x * lista2.count(x) for x in lista1)}")
    else:
        print("No existe esa parte")

    