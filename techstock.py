# ==========================================
# TechStock - Controle de estoque TechPoint
# Aluno(a): Paulo Henrique Martins]
# ==========================================


print("==========================================")
print("              TECHSTOCK 2.0               ")
print("                TECHPOINT                 ")
print("==========================================")

# cadastro do produto
codigo = input("Código do produto: ")
nome = input("Nome do produto: ")

preco = float(input("Preço de venda (R$): "))
while preco <= 0:
    print("ERRO: o preço precisa ser maior que zero.")
    preco = float(input("Preço de venda (R$): "))

quantidade = int(input("Quantidade em estoque: "))
while quantidade < 0:
    print("ERRO: a quantidade não pode ser negativa.")
    quantidade = int(input("Quantidade em estoque: "))

estoque_minimo = int(input("Estoque mínimo: "))
while estoque_minimo < 0:
    print("ERRO: o estoque mínimo não pode ser negativo.")
    estoque_minimo = int(input("Estoque mínimo: "))

print("Produto cadastrado!")

# contadores e acumuladores
qtd_entradas = 0
qtd_vendas = 0
unidades_vendidas = 0
faturamento = 0.0

# menu principal
opcao = ""
while opcao != "0":
    print()
    print("============ MENU ============")
    print("[1] Registrar entrada")
    print("[2] Registrar venda")
    print("[3] Vendas em sequência")
    print("[4] Ficha do produto")
    print("[5] Gráfico do estoque")
    print("[6] Inventário por prateleira")
    print("[7] Relatório do dia")
    print("[0] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        entrada = int(input("Quantas unidades chegaram? "))
        while entrada <= 0:
            print("ERRO: digite um valor maior que zero.")
            entrada = int(input("Quantas unidades chegaram? "))
        quantidade = quantidade + entrada
        qtd_entradas = qtd_entradas + 1
        print("Entrada registrada. Estoque atual:", quantidade)

    elif opcao == "2":
        if quantidade == 0:
            print("Produto SEM ESTOQUE. Não é possível vender.")
        else:
            saida = int(input("Quantas unidades foram vendidas? "))
            while saida <= 0 or saida > quantidade:
                print("ERRO: digite um valor entre 1 e", quantidade)
                saida = int(input("Quantas unidades foram vendidas? "))
            quantidade = quantidade - saida
            qtd_vendas = qtd_vendas + 1
            unidades_vendidas = unidades_vendidas + saida
            faturamento = faturamento + (saida * preco)
            print("Venda registrada. Estoque atual:", quantidade)

    elif opcao == "3":
        total = int(input("Quantas vendas você quer registrar? "))
        for i in range(1, total + 1):
            if quantidade == 0:
                print("O estoque acabou! Encerrando as vendas.")
                break
            print("Venda", i)
            saida = int(input("Unidades vendidas: "))
            if saida <= 0 or saida > quantidade:
                print("Venda ignorada: valor inválido.")
                continue
            quantidade = quantidade - saida
            qtd_vendas = qtd_vendas + 1
            unidades_vendidas = unidades_vendidas + saida
            faturamento = faturamento + (saida * preco)
            print("Venda", i, "registrada. Estoque atual:", quantidade)

    elif opcao == "4":
        valor_total = round(preco * quantidade, 2)
        print()
        print("------------------------------------------")
        print("FICHA DO PRODUTO")
        print("Código:", codigo)
        print("Produto:", nome)
        print("Preço: R$", preco)
        print("Em estoque:", quantidade, "unidade(s)")
        print("Estoque mínimo:", estoque_minimo)
        print("Valor total em estoque: R$", valor_total)

        if quantidade == 0:
            print("Situação: SEM ESTOQUE - repor urgente!")
        elif quantidade < estoque_minimo:
            faltam = estoque_minimo - quantidade
            print("Situação: ESTOQUE BAIXO - repor pelo menos", faltam, "unidade(s)")
        else:
            print("Situação: ESTOQUE OK")

        print("------------------------------------------")

    elif opcao == "5":
        barra = ""
        for i in range(quantidade):
            barra = barra + "#"

        marca = ""
        for i in range(estoque_minimo):
            marca = marca + "#"

        print("Estoque:", barra, quantidade)
        print("Mínimo: ", marca, estoque_minimo)

    elif opcao == "6":
        prateleiras = int(input("Quantas prateleiras guardam o produto? "))
        caixas = int(input("Quantas caixas tem cada prateleira? "))
        total_contado = 0

        for p in range(1, prateleiras + 1):
            soma_prateleira = 0
            for c in range(1, caixas + 1):
                print("Prateleira", p, "- caixa", c)
                unidades = int(input("Unidades na caixa: "))
                soma_prateleira = soma_prateleira + unidades
            print("Total da prateleira", p, "=", soma_prateleira)
            total_contado = total_contado + soma_prateleira

        print("Total contado:", total_contado, "| No sistema:", quantidade)
        if total_contado == quantidade:
            print("Contagem confere com o sistema!")
        else:
            diferenca = total_contado - quantidade
            quantidade = total_contado
            print("Diferença de", diferenca, "unidade(s). Estoque ajustado.")

    elif opcao == "7":
        print()
        print("---- RELATÓRIO DO DIA ----")
        print("Entradas registradas:", qtd_entradas)
        print("Vendas registradas:", qtd_vendas)
        print("Unidades vendidas:", unidades_vendidas)
        print("Faturamento: R$", round(faturamento, 2))
        if qtd_vendas > 0:
            media = unidades_vendidas / qtd_vendas
            print("Média por venda:", round(media, 1), "unidade(s)")
        else:
            print("Média por venda: 0 unidade(s)")
        print("---------------------------")

    elif opcao == "0":
        print("Encerrando o TechStock... até logo!")

    else:
        print("Opção inválida. Tente de novo.")
        
# REGISTRO ETAPA 3
# 1) len(produtos) mede quantos produtos diferentes estão cadastrados.
# 2) usamos indice + 1 porque o índice começa em 0 e para o usuário a numeração começa em 1.
# 3) usamos numero - 1 porque o usuário digita a partir de 1, mas a lista no Python começa no índice 0.
# 4) consegui testar a listagem numerada, o aviso de SEM ESTOQUE, o contador de menos de 5 unidades e a consulta pela posição.

produtos = []

# listagem numerada
if not produtos:
    print("Nenhum produto cadastrado.")
else:
    print("\n=== PRODUTOS CADASTRADOS ===")
    for indice in range(len(produtos)):
        produto = produtos[indice]
        situacao = ""
        if produto["quantidade"] == 0:
            situacao = " | SEM ESTOQUE"
        print(
            f'{indice + 1} {produto["nome"]} | '
            f'Qtd: {produto["quantidade"]} | '
            f'R$ {produto["preco"]}{situacao}'
        )
    print(f"Tipos de produtos: {len(produtos)}")
    baixo = 0
    for indice in range(len(produtos)):
        if produtos[indice]["quantidade"] < 5:
            baixo = baixo + 1
    print("Produtos com menos de 5 unidades:", baixo)

# consultar pela posição
if not produtos:
    print("Nenhum produto cadastrado.")
else:
    print("\n=== PRODUTOS CADASTRADOS ===")
    for indice in range(len(produtos)):
        produto = produtos[indice]
        situacao = ""
        if produto["quantidade"] == 0:
            situacao = " | SEM ESTOQUE"
        print(
            f'{indice + 1} {produto["nome"]} | '
            f'Qtd: {produto["quantidade"]} | '
            f'R$ {produto["preco"]}{situacao}'
        )
    print(f"Tipos de produtos: {len(produtos)}")
    texto = input("Digite o número do produto: ")
    if not texto.isdigit():
        print("Digite um número inteiro válido.")
    else:
        numero = int(texto)
        if numero < 1 or numero > len(produtos):
            print("Produto fora da lista.")
        else:
            produto = produtos[numero - 1]
            print(f'Produto: {produto["nome"]}')
            print(f'Quantidade: {produto["quantidade"]}')
            print(f'Preço: R$ {produto["preco"]}')
            total = produto["quantidade"] * produto["preco"]
            print(f"Valor total: R$ {total}")