aux = input("Distancia (m): ")
distancia = float(aux)

tempo = float(input("Tempo (s): "))
velocidade_ms = distancia / tempo

distancia_km = distancia / 1000
tempo_h = tempo / 3600

velocidade_kmh = distancia_km / tempo_h

print(f"Velocidade m/s: {velocidade_ms}")
print(f"Velocidade km/h: {velocidade_kmh}")
