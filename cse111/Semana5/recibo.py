import csv

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
    dic_produtos = ler_dicionario("produtos.csv", 0)

    print("Todos os produtos")
    print(dic_produtos)

    print()
    print("Itens pedidos")

    with open("pedido.csv", "rt", encoding="utf-8") as arquivo_pedido:
        leitor = csv.reader(arquivo_pedido)

        next(leitor)

        for linha in leitor:
            id_produto = linha[0]
            quantidade = linha[1]

            produto = dic_produtos[id_produto]

            nome = produto[1]
            preco = produto[2]

            print(f"{nome}: {quantidade} @ {preco}")


if __name__ == "__main__":
    main()