def obtenemos_resultados(nums):
    # Añadimos el primer número
    resultados = [nums[0]]
    # procesamos cada número a partir del segundo
    for num in nums[1:]:
        resultados_aux = []
        for val in resultados:
            # opción con suma
            resultados_aux.append(val + num)
            # opción con multiplicación
            resultados_aux.append(val * num)
        resultados = resultados_aux  # actualizamos resultados parciales

    return resultados

def obtenemos_resultados_2(nums):
    # Añadimos el primer número
    resultados = [nums[0]]
    # procesamos cada número a partir del segundo
    for num in nums[1:]:
        resultados_aux = []
        for val in resultados:
            # opción con suma
            resultados_aux.append(val + num)
            # opción con multiplicación
            resultados_aux.append(val * num)
            # opción con ||
            resultados_aux.append(int(str(val)+ str(num)))
        resultados = resultados_aux  # actualizamos resultados parciales

    return resultados

def resolver( parte: int, iterador ):

    #Tenemos que leer líneas similares a 3267: 81 40 27
    #El valor anterior a los puntos es el posible resultado de combinaciones de + o *, y en el caso de la parte 2 también la concatenación del resultado anterior
    # con el valor siguiente, de los valores siguientes
    matriz = []
    for linea in iterador:
            aux = linea.split(':')
            aux2 = [ int(x) for x in aux[1].strip().split(" ")]
            matriz.append((int(aux[0]), aux2))
    if parte == 1:
        print(f"El resultado de día 7 parte 1 es {sum( x[0] for x in matriz if x[0] in obtenemos_resultados(x[1]))}")    
    elif parte == 2:
        print(f"El resultado de día 7 parte 2 es {sum( x[0] for x in matriz if x[0] in obtenemos_resultados_2(x[1]))}")
    else:
        print("No existe esa parte")

    