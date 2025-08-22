# line_reader.py

from typing import Iterator


class LineReader:
    """
    Clase para leer un fichero de texto línea a línea
    usando un generador (yield).
    """

    def __init__(self, filepath: str, encoding: str = "utf-8") -> None:
        self.filepath = filepath
        self.encoding = encoding

    def lines(self) -> Iterator[str]:
        """Generador que devuelve el fichero línea a línea como str."""
        with open(self.filepath, "r", encoding=self.encoding) as f:
            for line in f:
                yield line.rstrip("\n")

    def __iter__(self) -> Iterator[str]:
        """Permite usar directamente: for linea in LineReader(...)."""
        return self.lines()
