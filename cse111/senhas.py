MINUSCULAS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

MAIUSCULAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

DIGITOS = ["0","1","2","3","4","5","6","7","8","9"]

ESPECIAIS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", 
             "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", 
             ">", "?", "/", "`", "~"]

def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas=False):

    with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
       for linha in arquivo:
            linha = linha.strip()

            if maiusculas_e_minusculas:
                if palavra == linha:
                   return True
       
            else:

               if palavra.lower() == linha.lower():
                  return True
            
            return False

def palavra_tem_caractere(palavra, lista_caracteres):
   
   for caractere in palavra:

      if caractere in lista_caracteres:
         return True
      
   return False

def calcular_complexidade(palavra):
   
   complexidade = 0

   if palavra_tem_caractere(palavra, MINUSCULAS):
      complexidade += 1

   if palavra_tem_caractere(palavra, MAIUSCULAS):
      complexidade += 1

   if palavra_tem_caractere(palavra, DIGITOS):
      complexidade += 1

   if palavra_tem_caractere(palavra, ESPECIAIS):
      complexidade += 1

   return complexidade

def validar_senha(senha, comprimento_min=10, comprimento_forte=16):
   
   if procurar_palavra(senha,"lista_de_palavras.txt"):
      print("A senha é uma palavra do dicionário e não é segura.")
      return 0
   
   if procurar_palavra(senha, "senhas_mais_comuns.txt", True):
      print("A senha é comumente usada e não é segura.")
      return 0
   
   if len(senha) < comprimento_min:
      print("A senha é muito curta e não é segura.")
      return 1
   
   if len(senha) >= comprimento_forte:
      print("A senha é longa, o comprimento supera a complexidade e é uma boa senha.")
      return 5
   
   complexidade = calcular_complexidade(senha)

   forca = complexidade + 1

   return forca

def main():
   
   while True:

      senha = input("Digite uma senha para testar (ou Q para sair): ")

      if senha.lower() == "q":
         print("Programa encerrado.")
         break

      forca = validar_senha(senha)

      print(f"Força da senha: {forca}")
      print()

if __name__ == "__main__":
   main()