def realizar_pedido(lista_pedidos, lista_itens, fila_pendentes):
    codigo = len(lista_pedidos) + 1
    cliente = input("Nome do cliente: ")
    pedido = {
        "codigo": codigo,
        "cliente": cliente,
        "itens": [],
        "total": 0,
        "status": "AGUARDANDO"
    }
    print("\nItens disponíveis para o pedido:")
    for item in lista_itens:
        print(f"Código: {item['codigo']}, Nome: {item['nome']}, Preço: R$ {item['preco']:.2f}, Estoque: {item['estoque']}")
    while True:
        cod = input("Informe o código do item para adicionar (ou ENTER para finalizar): ")
        if cod == "":
            break
        try:
            cod = int(cod)
        except ValueError:
            print("Código inválido!")
            continue
        item_encontrado = None
        for item in lista_itens:
            if item["codigo"] == cod:
                item_encontrado = item
                break
        if not item_encontrado:
            print("Item não encontrado!")
            continue
        qtd = input(f"Quantidade de '{item_encontrado['nome']}': ")
        try:
            qtd = int(qtd)
        except ValueError:
            print("Quantidade inválida!")
            continue
        if qtd > item_encontrado["estoque"]:
            print("Quantidade solicitada maior que estoque disponível!")
            continue
        item_encontrado["estoque"] -= qtd
        pedido["itens"].append({
            "codigo": item_encontrado["codigo"],
            "nome": item_encontrado["nome"],
            "preco": item_encontrado["preco"],
            "quantidade": qtd
        })
        pedido["total"] += item_encontrado["preco"] * qtd
        print(f"Item '{item_encontrado['nome']}' adicionado ao pedido.")
    if pedido["itens"]:
        lista_pedidos.append(pedido)
        fila_pendentes.append(pedido)
        print("Pedido registrado com sucesso!")

def processar_pedido(fila_pendentes, fila_aceitos):
    if not fila_pendentes:
        print("Nenhum pedido pendente.")
        return
    pedido = fila_pendentes.pop(0)
    print(f"Processando pedido: {pedido['codigo']} - {pedido['cliente']}")
    print(f"Valor total: R$ {pedido['total']:.2f}")
    acao = input("Aceitar (A) ou Rejeitar (R)? ").upper()
    if acao == "A":
        pedido["status"] = "ACEITO"
        fila_aceitos.append(pedido)
        print("Pedido aceito.")
    else:
        pedido["status"] = "REJEITADO"
        print("Pedido rejeitado.")

def atualizar_status_pedido(pedidos, fila_aceitos, fila_prontos):
    codigo = int(input("Código do pedido: "))
    for pedido in pedidos:
        if pedido["codigo"] == codigo:
            print("Status atual:", pedido["status"])
            novo = input("Novo status: ")
            pedido["status"] = novo
            if novo == "FAZENDO" and pedido in fila_aceitos:
                fila_aceitos.remove(pedido)
                fila_prontos.append(pedido)
            print("Status atualizado!")
            return
    print("Pedido não encontrado.")

def cancelar_pedido(pedidos):
    codigo = int(input("Código do pedido: "))
    for pedido in pedidos:
        if pedido["codigo"] == codigo:
            if pedido["status"] in ["AGUARDANDO", "ACEITO"]:
                pedido["status"] = "CANCELADO"
                print("Pedido cancelado!")
            else:
                print("Não é possível cancelar este pedido.")
            return
    print("Pedido não encontrado.")

def listar_pedidos(lista_pedidos):
    if not lista_pedidos:
        print("Nenhum pedido cadastrado!")
        return
    print("\n--- PEDIDOS ---")
    for pedido in lista_pedidos:
        print(f"Código: {pedido['codigo']}, Cliente: {pedido['cliente']}, Total: R$ {pedido['total']:.2f}, Status: {pedido['status']}")
        if pedido["itens"]:
            print("  Itens do pedido:")
            for item in pedido["itens"]:
                print(f"    - {item['quantidade']}x {item['nome']} (R$ {item['preco']:.2f} cada)")

def relatorio_pedidos(pedidos, fila_pendentes, fila_aceitos, fila_prontos):
    print("\n--- RELATÓRIO ---")
    print(f"Pedidos cadastrados: {len(pedidos)}")
    print(f"Pedidos pendentes: {len(fila_pendentes)}")
    print(f"Pedidos aceitos: {len(fila_aceitos)}")
    print(f"Pedidos prontos: {len(fila_prontos)}")
    total_vendas = sum(p["total"] for p in pedidos if p["status"] == "ENTREGUE")
    print(f"Total em vendas entregues: R$ {total_vendas:.2f}")