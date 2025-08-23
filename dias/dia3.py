import re

def resolver( parte: int, iterador ):
    if parte == 1:
        #De una línea como esta:
        #"xmul(2,4)% not_mul(5,5) mul(32,64] then(mul(11,8)mul(8,5))"
        #Debemos obtener los mul(x,y) correctos, multiplicar esos pares y luego la suma del total

        #Vamos a trabajar con una expresión regular
        # Buscar solo mul(x,y) válidos (con paréntesis correctos)
        pat = r'mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)'
        total = 0
        
        for linea in iterador:
            # Encontrar todos los pares (x,y)
            mults = re.findall(pat, linea)
            total += sum(int(a) * int(b) for a, b in mults)
        
        print(f"El resultado de día 3 parte 1 es {total}")    
    
    elif parte == 2:
        #Ahora nos vamos a encontrar con don't(), que deshabilitará los mul que encontremos, y con do(), que habilitartá los
        #mul que encontremos.

        #Tenemos que cambiar el pat. Luego trabajaremos con un activo que nos indicará si seguimos sumando las multiplicaciones
        pat = r'mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)|do\(\)|don\'t\(\)'
        total = 0
        activo = True  # indica si los mul los tenemos en cuenta o no al haber encontrado previamente un don't
        for linea in iterador:
            matches = re.finditer(pat, linea)
            for m in matches:
                if m.group(1) and m.group(2):
                    # Es un mul(x,y)
                    if activo: total += int(m.group(1)) * int(m.group(2))
                else:
                    # Es do() o don't()
                    if m.group(0) == "do()":
                        activo = True
                    elif m.group(0) == "don't()":
                        activo = False
       
        print(f"El resultado de día 3 parte 2 es {total} ")
    else:
        print("No existe esa parte")

    