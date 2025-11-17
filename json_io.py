import json

def carregar_dados():
    try:
        with open("dados.json", "r") as f:
            data = json.load(f)
            return data.get("itens", []), data.get("pedidos", [])
    except Exception:
        return [], []

def salvar_dados(itens, pedidos):
    with open("dados.json", "w") as f:
        json.dump({
            "itens": itens,
            "pedidos": pedidos
        }, f, indent=4)