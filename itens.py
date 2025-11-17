def registrar_item(lista_itens):
    codigo = len(lista_itens) + 1
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))

    item = {
        "codigo": codigo,
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "estoque": estoque
    }

    lista_itens.append(item)
    print("Item registrado!")

def atualizar_item(lista_itens):
    codigo = int(input("Código do item a atualizar: "))
    for item in lista_itens:
        if item["codigo"] == codigo:
            print("Item atual:", item)
            item["nome"] = input("Novo nome: ")
            item["descricao"] = input("Nova descrição: ")
            item["preco"] = float(input("Novo preço: "))
            item["estoque"] = int(input("Novo estoque: "))
            print("Item atualizado!")
            return
    print("Item não encontrado.")

def listar_itens(lista_itens):
    if not lista_itens:
        print("Nenhum item cadastrado!")
        return
    print("\n--- ITENS CADASTRADOS ---")
    for item in lista_itens:
        print(f"Código: {item['codigo']}, Nome: {item['nome']}, Preço: R$ {item['preco']:.2f}, Estoque: {item['estoque']}")