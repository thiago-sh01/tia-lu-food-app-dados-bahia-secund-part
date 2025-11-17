# tia-lu-food-app-dados-bahia-secund-part
🍔 Sistema de Gerenciamento de Pedidos
👥 Equipe

Aloisio Caldas da Silva Junior

Eduardo Sousa da Silva

Eveny Castro de Almeida

Iran Pablo Santos Martins

Thiago Sanches Hohlenwerger

📖 Descrição

Este projeto é um sistema de gerenciamento de pedidos desenvolvido em Python, com o objetivo de simular o funcionamento básico de um restaurante. Ele utiliza estruturas de dados nativas para representar filas de pedidos e operações de gerenciamento de itens e pedidos.
O sistema é operado por meio de um menu interativo no terminal, permitindo manipular tanto o menu de itens quanto o fluxo dos pedidos.

⚙️ Estrutura e Funcionalidades
🔹 Gerenciamento de Itens do Menu

Cadastrar Item: Adiciona um novo produto ao menu.

Atualizar Item: Modifica nome, descrição, preço ou quantidade em estoque.

Consultar Itens: Exibe todos os itens cadastrados.

Cada item contém:

código – gerado automaticamente

nome

descrição

preço

estoque

🔹 Gerenciamento de Pedidos
Criar Pedido

Deve conter ao menos um item.

Pode incluir cupom de desconto.

O pedido é criado como pago e inicia no status AGUARDANDO APROVAÇÃO.

Processar Pedidos Pendentes

Permite aceitar ou rejeitar pedidos em ordem de chegada (FIFO).

Atualizar Status

Altera o status de um pedido conforme o fluxo definido.

Cancelar Pedido

Permitido apenas se o status for AGUARDANDO APROVAÇÃO ou ACEITO.

🔹 Fluxo de Filas de Pedidos

O sistema usa filas para organizar o fluxo:

Fila de Pedidos Pendentes: onde todos os pedidos começam.

Fila de Pedidos Aceitos: pedidos aceitos passam para status FAZENDO.

Fila de Pedidos Prontos: pedidos preparados mudam para FEITO e aguardam entrega (ESPERANDO ENTREGADOR).

🔹 Status Possíveis de um Pedido

AGUARDANDO APROVACAO

ACEITO

FAZENDO

FEITO

ESPERANDO ENTREGADOR

SAIU PARA ENTREGA

ENTREGUE

CANCELADO

REJEITADO

🔹 Consultas

O sistema permite:

Exibir todos os pedidos registrados.

Filtrar pedidos por status.

🛠️ Tecnologias Utilizadas

Python 3.x

Estruturas de dados nativas (list, queue)

Menu interativo no terminal
