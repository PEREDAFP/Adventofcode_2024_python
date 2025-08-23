def resolver( parte: int, iterador ):
    
    #Almacenamos los resultados obtenidos para luego contar cuantos registros cumplen ser seguros o no
    resultados = []
        
    if parte == 1:
        #Debemos comprobar que la diferencia entre los distintos números de la lista siempre crece o decrece
        #Y esa diferencia no puede ser superior a 3 o -3
        for linea in iterador:
            lista = [int(x) for x in linea.split(" ")]
            lista = [ b - a for a,b in zip(lista, lista[1:])]
            resultados.append(int ( all ( -3 <= d <= -1 for d in lista)) or ( all ( 1 <= d <= 3 for d in lista)))
               
        print(f"El resultado de día 2 parte 1 es {sum(resultados)} ")    
    elif parte == 2:
        #Lo mismo que la parte 1, pero ahora tendremos en cuenta los que cumplan la condición, además, si quitamos uno de los
        #elementos
        for linea in iterador:
            lista = [int(x) for x in linea.split(" ")]
            comprobamos = [ b - a for a,b in zip(lista, lista[1:])]
            #Ahora comprobamos si cumple la primera condición
            if ( all ( -3 <= d <= -1 for d in comprobamos)) or ( all ( 1 <= d <= 3 for d in comprobamos)):
                resultados.append(1)
            else:
            #Si no ha cumplido la primera condición iremos comprobando para todas combinaciones de la lista eliminando un
            #elemento. Para eso llevaremos un contador que inicializaremos a cero. Si en alguna de las combinaciones se cumple, pondremos
            # el contador a 1 y saldremos del bucle
            # 
            # Hacemos todas las posibles combinaciones
                contador = 0          
                for i in range(len(lista)):
                    combinacion = lista[:i] + lista[i+1:]
                    comprobamos = [ b - a for a,b in zip(combinacion, combinacion[1:])]
                    if (all(-3 <= d <= -1 for d in comprobamos) or all(1 <= d <= 3 for d in comprobamos)):
                        contador = 1
                        break
                resultados.append(contador)
                
        print(f"El resultado de día 2 parte 2 es {sum(resultados)} ")   
    else:
        print("No existe esa parte")

    