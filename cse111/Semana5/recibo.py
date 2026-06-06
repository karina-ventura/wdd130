# Foi adicionado ao programa a exibição da data limite para devolução.
# A data é definida automaticamente para 30 dias após a compra, às 21h.

import csv
from datetime import datetime, timedelta

def ler_dicionario(filename, indice_coluna_chave):
    dicionario = {}

    with open(filename, "rt", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            chave = linha[indice_coluna_chave]
            dicionario[chave] = linha

    return dicionario

def main():

    try:

        dic_produtos = ler_dicionario("produtos.csv", 0)

        print("Ponto Certo Mercearia")
        print()

        numero_itens = 0
        subtotal = 0

        print()
        print("Itens pedidos")

        with open("pedido.csv", "rt", encoding="utf-8") as arquivo_pedido:
            leitor = csv.reader(arquivo_pedido)

            next(leitor)

            for linha in leitor:
                id_produto = linha[0]
                quantidade = int(linha[1])

                produto = dic_produtos[id_produto]

                nome = produto[1]
                preco = float(produto[2])

                print(f"{nome}: {quantidade} @ {preco:.2f}")

                numero_itens += quantidade
                subtotal += quantidade * preco

        imposto = subtotal * 0.06
        total = subtotal + imposto

        print()
        print(f"Número de itens: {numero_itens}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Imposto sobre vendas: {imposto:.2f}")
        print(f"Total: {total:.2f}")

        print()
        print("Obrigado por comprar no Ponto Certo Mercearia.")

        agora = datetime.now()
        print(agora.strftime("%d/%m/%Y %H:%M:%S"))

        print()
        print("Data limite para devolução: ")
        data_devolucao = agora + timedelta(days=30)
        data_devolucao = data_devolucao.replace(hour=21, minute=0, second=0)
        print(data_devolucao.strftime("%d/%m/%Y %H:%M:%S"))

    except FileNotFoundError as erro:
        print("Error: missing file")
        print(erro)

    except PermissionError as erro:
        print("Error: permission denied")
        print(erro)

    except KeyError as erro:
        print("Error: unknown product ID in the request.csv file")
        print(erro)


if __name__ == "__main__":
    main()