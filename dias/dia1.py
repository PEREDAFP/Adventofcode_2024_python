def resolver( parte: int, iterador ):

    if parte == 1:
        for linea in iterador:
            print(f"-> {linea}")
    elif parte == 2:
        print("Resolvemos parte 2")
    else:
        print("No existe esa parte")

    print(parte)