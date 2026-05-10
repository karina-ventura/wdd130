import math
from datetime import datetime

largura = int(input("Digite a largura do pneu em mm (por exemplo: 205): "))
proporcao = int(input("Digite a proporção do pneu (por exemplo: 60): "))
diametro = int(input("Digite o diâmetro da roda em polegadas (por exemplo: 15): "))

parte1 = math.pi * largura ** 2
parte2 = largura * proporcao + 2540 * diametro

volume = (parte1 * proporcao * parte2) / 10000000000

print(f"O volume aproximado é de {volume:.2f} litros")

data_atual = datetime.now()

with open("volumes.txt", "a", encoding="utf-8") as arquivo:
    print(f"{data_atual:%d-%m-%Y}, {largura}, {proporcao}, {diametro}, {volume:.2f}", file=arquivo)
