# ==========================================
# TechStock - Controle de estoque TechPoint
# Aluno(a): Paulo Henrique Martins]
# ==========================================


print("==========================================")
print("                TECHSTOCK                 ")
print("                TECHPOINT                 ")
print("==========================================")

produtos = []

qtd_entradas = 0
qtd_vendas = 0
unidades_vendidas = 0
faturamento = 0

opcao = ""
while opcao != "0":
    print()
    print("============ MENU ============")
    print("[1] Cadastrar produto")
    print("[2] Registrar entrada")
    print("[3] Registrar venda")
    print("[4] Listar produtos")
    print("[5] Gráfico do estoque")
    print("[6] Inventário por prateleira")
    print("[7] Relatório do dia")
    print("[10] Buscar produto por código")
    print("[11] Atualizar dados do produto")
    print("[12] Relatório geral do estoque")
    print("[0] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = int(input("Código do produto: "))
        codigo_existe = False
        for produto in produtos:
            if produto["codigo"] == codigo:
                codigo_existe = True
                break
        if codigo_existe:
            print("Código já cadastrado!")
        else:
            nome = input("Nome: ")
            quantidade = int(input("Quantidade: "))
            while quantidade < 0:
                print("ERRO: a quantidade não pode ser negativa.")
                quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            while preco <= 0:
                print("ERRO: o preço precisa ser maior que zero.")
                preco = float(input("Preço: "))
            novo = {
                "codigo": codigo,
                "nome": nome,
                "quantidade": quantidade,
                "preco": preco
            }
            produtos.append(novo)
            print("Produto cadastrado!")

    elif opcao == "2":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for indice in range(len(produtos)):
                produto = produtos[indice]
                print(
                    f'{indice + 1} {produto["nome"]} | '
                    f'Qtd: {produto["quantidade"]} | '
                    f'R$ {produto["preco"]:.2f}'
                )
            num = int(input("Escolha o número do produto: "))
            if num < 1 or num > len(produtos):
                print("Produto fora da lista.")
            else:
                produto = produtos[num - 1]
                entrada = int(input("Quantas unidades chegaram? "))
                while entrada <= 0:
                    print("ERRO: digite um valor maior que zero.")
                    entrada = int(input("Quantas unidades chegaram? "))
                produto["quantidade"] = produto["quantidade"] + entrada
                qtd_entradas = qtd_entradas + 1
                print("Entrada registrada. Estoque atual:", produto["quantidade"])

    elif opcao == "3":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for indice in range(len(produtos)):
                produto = produtos[indice]
                print(
                    f'{indice + 1} {produto["nome"]} | '
                    f'Qtd: {produto["quantidade"]} | '
                    f'R$ {produto["preco"]:.2f}'
                )
            num = int(input("Escolha o número do produto: "))
            if num < 1 or num > len(produtos):
                print("Produto fora da lista.")
            else:
                produto = produtos[num - 1]
                if produto["quantidade"] == 0:
                    print("Produto SEM ESTOQUE. Não é possível vender.")
                else:
                    saida = int(input("Quantas unidades foram vendidas? "))
                    while saida <= 0 or saida > produto["quantidade"]:
                        print("ERRO: digite um valor entre 1 e", produto["quantidade"])
                        saida = int(input("Quantas unidades foram vendidas? "))
                    produto["quantidade"] = produto["quantidade"] - saida
                    qtd_vendas = qtd_vendas + 1
                    unidades_vendidas = unidades_vendidas + saida
                    faturamento = faturamento + (saida * produto["preco"])
                    print("Venda registrada. Estoque atual:", produto["quantidade"])

    elif opcao == "4":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\n=== PRODUTOS CADASTRADOS ===")
            baixo = 0
            for indice in range(len(produtos)):
                produto = produtos[indice]
                situacao = ""
                if produto["quantidade"] == 0:
                    situacao = " | SEM ESTOQUE"
                if produto["quantidade"] < 5:
                    baixo = baixo + 1
                print(
                    f'{indice + 1} {produto["nome"]} | '
                    f'Qtd: {produto["quantidade"]} | '
                    f'R$ {produto["preco"]:.2f}{situacao}'
                )
            print(f"Tipos de produtos: {len(produtos)}")
            print("Produtos com menos de 5 unidades:", baixo)

    elif opcao == "5":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for indice in range(len(produtos)):
                produto = produtos[indice]
                barra = ""
                for i in range(produto["quantidade"]):
                    barra = barra + "#"
                print(produto["nome"], barra, produto["quantidade"])

    elif opcao == "6":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for indice in range(len(produtos)):
                produto = produtos[indice]
                print(
                    f'{indice + 1} {produto["nome"]} | '
                    f'Qtd: {produto["quantidade"]} | '
                    f'R$ {produto["preco"]:.2f}'
                )
            num = int(input("Escolha o número do produto: "))
            if num < 1 or num > len(produtos):
                print("Produto fora da lista.")
            else:
                produto = produtos[num - 1]
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
                print("Total contado:", total_contado, "| No sistema:", produto["quantidade"])
                if total_contado == produto["quantidade"]:
                    print("Contagem confere com o sistema!")
                else:
                    diferenca = total_contado - produto["quantidade"]
                    produto["quantidade"] = total_contado
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

    elif opcao == "10":
        codigo_busca = int(input("Código para buscar: "))
        encontrado = None
        for produto in produtos:
            if produto["codigo"] == codigo_busca:
                encontrado = produto
                break
        if encontrado is None:
            print("Produto não encontrado.")
        else:
            print("Nome:", encontrado["nome"])
            print("Quantidade:", encontrado["quantidade"])
            print(f"Preço: R$ {encontrado['preco']:.2f}")
            total = encontrado["quantidade"] * encontrado["preco"]
            print(f"Valor total: R$ {total:.2f}")

    elif opcao == "11":
        codigo_busca = int(input("Código do produto: "))
        encontrado = None
        for produto in produtos:
            if produto["codigo"] == codigo_busca:
                encontrado = produto
                break
        if encontrado is None:
            print("Produto não encontrado.")
        else:
            print("1 - Alterar nome")
            print("2 - Alterar quantidade")
            escolha = input("Escolha: ")
            if escolha == "1":
                encontrado["nome"] = input("Novo nome: ")
                print("Nome atualizado!")
            elif escolha == "2":
                nova_qtd = int(input("Nova quantidade: "))
                if nova_qtd < 0:
                    print("Quantidade inválida!")
                else:
                    encontrado["quantidade"] = nova_qtd
                    print("Quantidade atualizada!")
            else:
                print("Opção inválida.")

    elif opcao == "12":
        total_estoque = 0
        print("====== RELATÓRIO GERAL ======")
        for produto in produtos:
            subtotal = produto["quantidade"] * produto["preco"]
            total_estoque += subtotal
            print(produto["codigo"], "-", produto["nome"])
            print("Quantidade:", produto["quantidade"])
            print(f"Preço unitário: R$ {produto['preco']:.2f}")
            print(f"Subtotal: R$ {subtotal:.2f}")
        print(f"Total do estoque: R$ {total_estoque:.2f}")

    elif opcao == "0":
        print("Saindo do TechStock...")

    else:
        print("Opção inválida. Tente de novo.")
