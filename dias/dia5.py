def resolver( parte: int, iterador ):
    orden = [] #Aquí se guardan los valores "91|77". Lo cambiamos a la forma (,)
    actualizaciones = [] #Aquí se guardan los valores "78,98,22,22,...." 
    for linea in iterador:
        if len(linea) == 5:
            orden.append(tuple(linea.split('|')))
        elif linea != "":
            actualizaciones.append(linea.split(','))
    
    if parte == 1:   
        total = 0 
        for linea in actualizaciones:
            #Hacemos todas las combinaciones posibles de esa línea invirtiendo el orden 
            combinaciones = [(linea[j],linea[i]) for i in range(len(linea)) for j in range(i + 1, len(linea))]
            incorrecto =  any(i in orden for i in combinaciones)
            if not (incorrecto): total += int(linea[len(linea)//2])
                
        print(f"El resultado de día 5 parte 1 es {total}")    
    
    elif parte == 2:
        total2 = 0
        for linea in actualizaciones:
            #Si es incorrecta la línea: cambiamos el orden y obtenemos el número del índice mitad
            #Tenemos que resolver el error, parece que hay que comprobar el primer cambio, luego el segundo...
            combinaciones = [(linea[j], linea[i]) for i in range(len(linea)) for j in range(i + 1, len(linea))]
            incorrecto = any(i in orden for i in combinaciones)
            primera_vez = True #Se utiliza para no calcular de nuevo combinaciones e incorrecto la primera vez

            while incorrecto:
                #Hacemos todas las combinaciones posibles de esa línea invirtiendo el orden 
                if not(primera_vez):
                    combinaciones = [(linea[j], linea[i]) for i in range(len(linea)) for j in range(i + 1, len(linea))]
                    incorrecto =  any(i in orden for i in combinaciones)      
                primera_vez = False  
               
                if incorrecto:  
                    valor1,valor2 = next( (i for i in combinaciones if i in orden), None)
                    #En vez de utilizar linea.index, hacemos esta virguería propuesta por deepseek
                    #Se consigue una mejora de un segundo menos...igual no es para tanto.  
                    #Y muy poco pythonico
                    #indice1 = next((i for i, v in enumerate(linea) if v == valor1), -1)
                    #indice2 = next((i for i, v in enumerate(linea) if v == valor2), -1)
                    indice1 = linea.index(valor1)
                    indice2 = linea.index(valor2)
                    linea[indice1], linea[indice2] = linea[indice2], linea[indice1]
                else:
                    total2 += int(linea[len(linea)//2])     
                
        print(f"El resultado de día 5 parte 2 es {total2}")
    else:
        print(orden)
        print(actualizaciones)
        print("No existe esa parte")

    