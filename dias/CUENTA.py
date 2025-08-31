mapa = [
"....XXXXX#",
"....#.....",
"....X...X.",
"..#.X...X.",
"..XXXXX#X.",
"..X.X.X.X.",
".#XXXXXXX.",
".XXXXXXX#.",
"#XXXXXXX..",
"......#X..",
]
cuenta = sum( fila.count('X')  for fila in mapa )

print(cuenta)