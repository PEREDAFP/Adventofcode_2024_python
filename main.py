import argparse
import sys
import importlib
from milib import LineReader


def main():
    parser = argparse.ArgumentParser(
        description="Lector de ficheros línea a línea con parámetros día y parte.",
        #add_help=True,    Descomentar si queremos utilizar la ayuda en inglés de argparse
    )

    parser.add_argument("--file", help="Ruta al fichero de entrada")
    parser.add_argument("--dia", type=int, help="Número de día (ej: 1, 2, 3...)")
    parser.add_argument("--parte", type=int, help="Número de parte en el día 1, o 2 generalmente")

    args = parser.parse_args()

    #Si no se ha introducido alguno de los parámetros salta y lo ponemos en español
    #Esto no sería necesario si queremos utilizar las ayudad de argparse por defecto
    if args.file is None or args.dia is None or args.parte is None:
        print(f"Error: Debes indicar --file, --dia y --parte", file=sys.stderr)
        print(f"{parser.prog} --file FILE --dia DIA --parte 1 ó 2", file=sys.stderr)
        sys.exit(2)

    # Si todo está bien

    #Obtenemos el resolver del día correspondiente con importlib
    nombre_modulo = f"dias.dia{args.dia}"
    
    try:
        modulo = importlib.import_module(nombre_modulo)
    except ModuleNotFoundError:
        print(f"No existe el módulo para el día {args.dia} ({nombre_modulo}.py).")
        sys.exit(2)

    # --- Ejecutar función resolver() si existe, que debe existir por estructura del código y se le pasará por parámetro la parte  ---
    if hasattr(modulo, "resolver"):
        #Leemos el fichero utilizando el iterador de LineReader y se lo pasamos a la función resolver
        reader = LineReader(args.file)
        modulo.resolver(args.parte, reader)
    else:
        print(f"El módulo {nombre_modulo} no define una función resolver().")
    
    
     

if __name__ == "__main__":
    main()
