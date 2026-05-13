"""Calcula e exiba o volume de um cone circular reto"""
 
# Importa módulo math padrão para que
# math.pi possa ser usado neste programa.
import math
 
 
def main():
# Chama a função volume_cone para calcular o volume
# de um cone, exemplificando como o programa funciona.
  ex_raio = 2.8
  ex_altura = 3.2
  ex_vol = volume_cone()
 
  # Exibe várias linhas que descrevem este programa.
  print("Este programa calcula o volume de um cone circular reto.")
  print(f"Por exemplo, se o raio de um cone é {ex_raio} e")
  print(f"a altura é {ex_altura} então o volume é {ex_vol:.1f}")
  print()
 
  # Obtém o raio e a altura do cone do usuário.
  raio = float(input("Por favor, digite o raio do cone: "))
  altura = float(input("Por favor, digite a altura do cone: "))
 
  # Chama a função volume_cone para calcular o volume
  # para o raio e a altura que vieram do usuário.
  vol = volume_cone()
 
  # Imprime o raio, a altura e
  # volume para o usuário ver.
  print(f"Raio: {raio}")
  print(f"Altura: {altura}")
  print(f"Volume: {vol:.1f}")
 
 
def volume_cone():
  """Calcula e retorna o volume de um cone circular reto"""
  volume = math.pi * raio**2 * altura / 3
  return volume
 
 
# Inicia este programa
# chamando a função main.
main()