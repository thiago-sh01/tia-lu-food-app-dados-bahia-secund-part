from json_io import carregar_dados, salvar_dados
from itens import registrar_item, atualizar_item, listar_itens
from pedidos import (
    realizar_pedido,
    processar_pedido,
    atualizar_status_pedido,
    cancelar_pedido,
    listar_pedidos,
    relatorio_pedidos
)
from ordenacao_bubble_sort import bubble_sort

# Inicializa
itens, pedidos = carregar_dados()
fila_pendentes = [p for p in pedidos if p["status"] == "AGUARDANDO"]
fila_aceitos   = [p for p in pedidos if p["status"] == "ACEITO"]
fila_prontos   = [p for p in pedidos if p["status"] == "FAZENDO"]

while True:
    print("\n==== SISTEMA DE PEDIDOS – LU DELIVERY ====")
    print("1 - Registrar Item")
    print("2 - Atualizar Item")
    print("3 - Listar Itens")
    print("4 - Criar Pedido")
    print("5 - Listar Pedidos (ordenados por código)")
    print("6 - Processar Pedido Pendente")
    print("7 - Atualizar Status de Pedido")
    print("8 - Cancelar Pedido")
    print("9 - Relatório")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_item(itens)

    elif opcao == "2":
        atualizar_item(itens)

    elif opcao == "3":
        listar_itens(itens)

    elif opcao == "4":
        realizar_pedido(pedidos, itens, fila_pendentes)

    elif opcao == "5":
        pedidos_ordenados = bubble_sort(pedidos)
        listar_pedidos(pedidos_ordenados)

    elif opcao == "6":
        processar_pedido(fila_pendentes, fila_aceitos)

    elif opcao == "7":
        atualizar_status_pedido(pedidos, fila_aceitos, fila_prontos)

    elif opcao == "8":
        cancelar_pedido(pedidos)

    elif opcao == "9":
        relatorio_pedidos(pedidos, fila_pendentes, fila_aceitos, fila_prontos)

    elif opcao == "0":
        salvar_dados(itens, pedidos)
        print("Saindo... Dados salvos!")
        break

    else:
        print("Opção inválida!")