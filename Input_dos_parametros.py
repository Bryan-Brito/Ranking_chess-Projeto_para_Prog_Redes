import Rating_fide

pontos = 5.0
num_partidas = int(10)
rating_oponentes = [2100, 2000, 2200, 1950, 2150, 2300, 2050, 1900, 2250, 2100]

rating = Rating_fide.calculo_fide(pontos, num_partidas, rating_oponentes)

print("O rating FIDE do jogador é:", rating)