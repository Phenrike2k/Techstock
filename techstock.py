# ============================================
# TechStock 6.0 - Controle de estoque TechPoint
# Aluno(a): Paulo Henrique Martins
# ============================================

produtos = [
    {
        "codigo": "M07",
        "nome": "Mouse Gamer",
        "quantidade": 12,
        "preco": 350.99,
        "estoque_minimo": 5
    },
    {
        "codigo": "T01",
        "nome": "Teclado",
        "quantidade": 4,
        "preco": 80.0,
        "estoque_minimo": 5
    },
    {
        "codigo": "MON01",
        "nome": "Monitor",
        "quantidade": 2,
        "preco": 500.0,
        "estoque_minimo": 5
    }
]

historico = []
fila_reposicao = []


# Exibe o menu principal.
def exibir_menu():
    print("============ MENU ============")
    print("[1] Cadastrar produto")
    print("[2] Registrar entrada")
    print("[3] Registrar venda")
    print("[4] Vendas em sequência")
    print("[5] Ficha do produto")
    print("[6] Gráfico do estoque")
    print("[7] Inventário por prateleira")
    print("[8] Alterar preço")
    print("[9] Excluir produto")
    print("[10] Buscar produto por código")
    print("[11] Atualizar nome ou quantidade")
    print("[12] Relatório geral do estoque")
    print("[17] Produtos com estoque baixo")
    print("[18] Desfazer última alteração")
    print("[19] Ver histórico")
    print("[20] Pedir reposição")
    print("[21] Receber próxima reposição")
    print("[22] Ver fila de reposição")
    print("[0] Sair")


# Busca um produto pelo código e devolve o dicionário ou None.
def buscar_produto(codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


# Mostra o nome, a quantidade e o preço de um produto.
def mostrar_produto(produto):
    print("Nome:", produto["nome"])
    print("Quantidade em estoque:", produto["quantidade"])
    print(f'Preço: R$ {produto["preco"]:.2f}')


# Calcula o subtotal de um produto no estoque.
def calcular_subtotal(produto):
    return produto["quantidade"] * produto["preco"]


# Guarda a quantidade de antes, para poder desfazer.
def registrar_historico(produto, descricao):
    registro = {
        "codigo": produto["codigo"],
        "quantidade_antes": produto["quantidade"],
        "descricao": descricao
    }
    historico.append(registro)


# Lê uma quantidade inteira positiva.
def ler_quantidade(mensagem):
    texto = input(mensagem).strip()
    while not texto.isdigit() or int(texto) <= 0:
        print("Digite um número inteiro. Ex: 15")
        texto = input(mensagem).strip()
    return int(texto)


# Cadastra um produto com código único.
def cadastrar_produto():
    texto_codigo = input("Código do produto: ").strip()
    if texto_codigo.isdigit():
        codigo = int(texto_codigo)
    else:
        codigo = texto_codigo

    if buscar_produto(codigo) is not None:
        print("Código já cadastrado!")
    else:
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

        novo = {
            "codigo": codigo,
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco,
            "estoque_minimo": estoque_minimo
        }
        produtos.append(novo)
        print("Produto cadastrado!")


# Lista os produtos com a posição, quantidade e preço.
def listar():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\n=== PRODUTOS CADASTRADOS ===")
    for indice in range(len(produtos)):
        produto = produtos[indice]
        situacao = ""
        if produto["quantidade"] == 0:
            situacao = " | SEM ESTOQUE"
        print(f'{indice + 1} - {produto["nome"]} | '
              f'Qtd: {produto["quantidade"]} | '
              f'R$ {produto["preco"]:.2f}{situacao}')
    print(f"Tipos de produtos: {len(produtos)}")

    baixo = 0
    for indice in range(len(produtos)):
        if produtos[indice]["quantidade"] < 5:
            baixo = baixo + 1
    print("Produtos com menos de 5 unidades:", baixo)


# Lista os produtos cuja quantidade está abaixo do estoque mínimo.
def listar_estoque_baixo():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    encontrou = False
    print("=== PRODUTOS COM ESTOQUE BAIXO ===")
    for indice in range(len(produtos)):
        produto = produtos[indice]
        if produto["quantidade"] < produto["estoque_minimo"]:
            print(f'{produto["codigo"]} - {produto["nome"]} | '
                  f'Estoque: {produto["quantidade"]} | '
                  f'Mínimo: {produto["estoque_minimo"]}')
            encontrou = True

    if not encontrou:
        print("Nenhum produto com estoque baixo.")


# Consulta um produto pela posição na lista e devolve seu dicionário.
def consultar_numero():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    listar()
    texto = input("Digite o número do produto: ")
    if not texto.isdigit():
        print("Digite um número inteiro válido.")
        return

    numero = int(texto)
    if numero < 1 or numero > len(produtos):
        print("Produto fora da lista.")
        return

    produto = produtos[numero - 1]
    mostrar_produto(produto)
    valor_total = calcular_subtotal(produto)
    print(f"Valor total em estoque: R$ {valor_total:.2f}")
    return produto


# Registra a entrada de unidades em um produto.
def registrar_entrada():
    produto = consultar_numero()
    if produto:
        entrada = int(input("Quantas unidades chegaram? "))
        while entrada <= 0:
            print("ERRO: digite um valor maior que zero.")
            entrada = int(input("Quantas unidades chegaram? "))
        registrar_historico(produto, "entrada")
        produto["quantidade"] = produto["quantidade"] + entrada
        print("Entrada registrada. Estoque atual:", produto["quantidade"])


# Registra uma venda de um produto.
def registrar_venda():
    produto = consultar_numero()
    if produto:
        if produto["quantidade"] == 0:
            print("Produto SEM ESTOQUE. Não é possível vender.")
        else:
            saida = int(input("Quantas unidades foram vendidas? "))
            while saida <= 0 or saida > produto["quantidade"]:
                print("ERRO: digite um valor entre 1 e", produto["quantidade"])
                saida = int(input("Quantas unidades foram vendidas? "))
            registrar_historico(produto, "saída")
            produto["quantidade"] = produto["quantidade"] - saida
            print("Venda registrada. Estoque atual:", produto["quantidade"])


# Registra várias vendas sequenciais de um produto.
def registrar_vendas_sequenciais():
    produto = consultar_numero()
    if produto:
        if produto["quantidade"] == 0:
            print("Produto SEM ESTOQUE. Não é possível vender.")
        else:
            total = int(input("Quantas vendas você quer registrar? "))
            for i in range(1, total + 1):
                if produto["quantidade"] == 0:
                    print("O estoque acabou! Encerrando as vendas.")
                    break
                print("Venda", i)
                saida = int(input("Unidades vendidas: "))
                if saida <= 0 or saida > produto["quantidade"]:
                    print("Venda ignorada: valor inválido.")
                    continue
                registrar_historico(produto, "saída")
                produto["quantidade"] = produto["quantidade"] - saida
                print("Venda", i, "registrada. Estoque atual:", produto["quantidade"])


# Exibe a ficha completa de um produto.
def exibir_ficha_produto():
    produto = consultar_numero()
    if produto:
        valor_total = round(calcular_subtotal(produto), 2)
        print()
        print("-------- FICHA DO PRODUTO --------")
        print("Código:", produto["codigo"])
        print("Produto:", produto["nome"])
        print("Preço: R$", produto["preco"])
        print("Em estoque:", produto["quantidade"], "unidade(s)")
        print("Estoque mínimo:", produto["estoque_minimo"])
        print("Valor total em estoque: R$", valor_total)
        if produto["quantidade"] == 0:
            print("Situação: SEM ESTOQUE - repor urgente!")
        elif produto["quantidade"] < produto["estoque_minimo"]:
            faltam = produto["estoque_minimo"] - produto["quantidade"]
            print("Situação: ESTOQUE BAIXO - repor pelo menos", faltam, "unidade(s)")
        else:
            print("Situação: ESTOQUE OK")
        print("----------------------------------")


# Exibe o gráfico de estoque de um produto.
def exibir_grafico_estoque():
    produto = consultar_numero()
    if produto:
        barra = ""
        for i in range(produto["quantidade"]):
            barra = barra + "#"
        marca = ""
        for i in range(produto["estoque_minimo"]):
            marca = marca + "#"
        print("Estoque:", barra, produto["quantidade"])
        print("Mínimo: ", marca, produto["estoque_minimo"])


# Confere e ajusta a quantidade de um produto no inventário físico.
def conferir_inventario():
    produto = consultar_numero()
    if produto:
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
            print("Diferença de", diferenca, "unidade(s). Estoque ajustado.")
            registrar_historico(produto, "ajuste de inventário")
            produto["quantidade"] = total_contado


# Altera o preço de venda de um produto.
def alterar_preco():
    texto_codigo = input("Código do produto para alterar o preço: ").strip()
    if texto_codigo.isdigit():
        codigo = int(texto_codigo)
    else:
        codigo = texto_codigo

    encontrado = buscar_produto(codigo)
    if encontrado is None:
        print("Produto não encontrado.")
    else:
        novo_preco = float(input("Novo preço de venda (R$): "))
        while novo_preco <= 0:
            print("ERRO: o preço precisa ser maior que zero.")
            novo_preco = float(input("Novo preço de venda (R$): "))
        encontrado["preco"] = novo_preco
        print("Preço atualizado.")


# Exclui um produto pelo código.
def excluir_produto():
    texto_codigo = input("Código do produto para excluir: ").strip()
    if texto_codigo.isdigit():
        codigo = int(texto_codigo)
    else:
        codigo = texto_codigo

    encontrado = buscar_produto(codigo)
    if encontrado is None:
        print("Produto não encontrado.")
    else:
        produtos.remove(encontrado)
        print("Produto excluído.")


# Consulta e mostra um produto pelo código.
def consultar_produto():
    texto_codigo = input("Código do produto para buscar: ").strip()
    if texto_codigo.isdigit():
        codigo = int(texto_codigo)
    else:
        codigo = texto_codigo

    encontrado = buscar_produto(codigo)
    if encontrado is None:
        print("Produto não encontrado.")
    else:
        mostrar_produto(encontrado)


# Atualiza o nome ou a quantidade de um produto pelo código.
def atualizar_produto():
    texto_codigo = input("Código do produto para atualizar: ").strip()
    if texto_codigo.isdigit():
        codigo = int(texto_codigo)
    else:
        codigo = texto_codigo

    encontrado = buscar_produto(codigo)
    if encontrado is None:
        print("Produto não encontrado.")
    else:
        print("[1] Atualizar nome")
        print("[2] Atualizar quantidade")
        campo = input("Escolha o que deseja atualizar: ")
        if campo == "1":
            encontrado["nome"] = input("Novo nome: ")
            print("Nome atualizado.")
        elif campo == "2":
            quantidade = int(input("Nova quantidade em estoque: "))
            if quantidade < 0:
                print("ERRO: a quantidade não pode ser negativa. Nada foi alterado.")
            else:
                registrar_historico(encontrado, "quantidade alterada")
                encontrado["quantidade"] = quantidade
                print("Quantidade atualizada.")
        else:
            print("Opção inválida.")


# Desfaz a última alteração de quantidade.
def desfazer():
    if len(historico) == 0:
        print("Nada para desfazer.")
        return

    ultimo = historico.pop()
    produto = buscar_produto(ultimo["codigo"])

    if produto is None:
        print("O produto dessa alteração não existe mais.")
        return

    produto["quantidade"] = ultimo["quantidade_antes"]
    print("Desfeito:", ultimo["descricao"], "-", produto["nome"])
    print("A quantidade voltou para", produto["quantidade"])


# Mostra o histórico do mais recente para o mais antigo.
def ver_historico():
    if len(historico) == 0:
        print("Histórico vazio.")
        return

    print("Do mais recente para o mais antigo:")
    for registro in reversed(historico):
        print(f"- {registro['descricao']} | código {registro['codigo']} | "
              f"antes: {registro['quantidade_antes']}")


# Coloca um pedido de reposição no fim da fila.
def pedir_reposicao():
    texto_codigo = input("Código do produto: ").strip()
    if texto_codigo.isdigit():
        codigo = int(texto_codigo)
    else:
        codigo = texto_codigo

    produto = buscar_produto(codigo)
    if produto is None:
        print("Produto não encontrado.")
        return

    quantidade = ler_quantidade("Quantas unidades pedir? ")
    pedido = {"codigo": codigo, "quantidade": quantidade}
    fila_reposicao.append(pedido)
    print("Pedido na fila. Posição:", len(fila_reposicao))


# Atende o primeiro pedido da fila.
def receber_reposicao():
    if len(fila_reposicao) == 0:
        print("Nenhum pedido na fila.")
        return

    pedido = fila_reposicao.pop(0)
    produto = buscar_produto(pedido["codigo"])

    if produto is None:
        print("O produto não existe mais. Pedido descartado.")
        return

    registrar_historico(produto, "reposição recebida")
    produto["quantidade"] = produto["quantidade"] + pedido["quantidade"]
    print("Chegaram", pedido["quantidade"], "unidade(s) de", produto["nome"])
    print("Pedidos restantes na fila:", len(fila_reposicao))


# Mostra os pedidos do primeiro para o último.
def ver_fila():
    if len(fila_reposicao) == 0:
        print("Fila de reposição vazia.")
        return

    for i in range(len(fila_reposicao)):
        pedido = fila_reposicao[i]
        print(f"{i + 1}º lugar | código {pedido['codigo']} | "
              f"{pedido['quantidade']} unidade(s)")


# Exibe o relatório geral e soma o valor do estoque.
def relatorio():
    total_estoque = 0
    print("====== RELATÓRIO GERAL ======")
    for produto in produtos:
        subtotal = calcular_subtotal(produto)
        total_estoque += subtotal
        print(produto["codigo"], "-", produto["nome"])
        print("  Quantidade:", produto["quantidade"])
        print(f'  Preço unitário: R$ {produto["preco"]:.2f}')
        print(f"  Subtotal: R$ {subtotal:.2f}")
    print(f"Total do estoque: R$ {total_estoque:.2f}")


# Executa o menu e encaminha cada opção para sua função.
opcao = ""
while opcao != "0":
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        registrar_entrada()
    elif opcao == "3":
        registrar_venda()
    elif opcao == "4":
        registrar_vendas_sequenciais()
    elif opcao == "5":
        exibir_ficha_produto()
    elif opcao == "6":
        exibir_grafico_estoque()
    elif opcao == "7":
        conferir_inventario()
    elif opcao == "8":
        alterar_preco()
    elif opcao == "9":
        excluir_produto()
    elif opcao == "10":
        consultar_produto()
    elif opcao == "11":
        atualizar_produto()
    elif opcao == "12":
        relatorio()
    elif opcao == "17":
        listar_estoque_baixo()
    elif opcao == "18":
        desfazer()
    elif opcao == "19":
        ver_historico()
    elif opcao == "20":
        pedir_reposicao()
    elif opcao == "21":
        receber_reposicao()
    elif opcao == "22":
        ver_fila()
    elif opcao == "0":
        print("Saindo do TechStock...")
    else:
        print("Opção inválida. Tente de novo.")
