# tia-lu-food-app-dados-bahia-secund-part
# 🍔 Sistema de Gerenciamento de Pedidos

## 👥 Equipe
- **Aloisio Caldas da Silva Junior**  
- **Eduardo Sousa da Silva**  
- **Eveny Castro de Almeida**  
- **Iran Pablo Santos Martins**  
- **Thiago Sanches Hohlenwerger**

---

## 📖 Descrição

Este projeto é um sistema de gerenciamento de pedidos desenvolvido em **Python**, simulando o funcionamento básico de um restaurante.  
Utiliza **estruturas de dados nativas** para representar filas, itens do menu e operações de gerenciamento de pedidos.  
A interação ocorre por meio de um **menu no terminal**, permitindo visualizar, atualizar e processar pedidos de forma dinâmica.

---

## ⚙️ Estrutura e Funcionalidades

### 🔹 Gerenciamento de Itens do Menu
- **Cadastrar Item:** adiciona um novo produto ao menu.  
- **Atualizar Item:** altera nome, descrição, preço ou estoque.  
- **Consultar Itens:** exibe todos os itens cadastrados.

**Cada item possui:**
- `código` (gerado automaticamente)  
- `nome`  
- `descrição`  
- `preço`  
- `estoque`  

---

### 🔹 Gerenciamento de Pedidos

**Criar Pedido**
- Deve conter pelo menos um item.
- Pode utilizar cupom de desconto.
- Inicia no status **AGUARDANDO APROVAÇÃO**.

**Processar Pedidos Pendentes**
- Permite aceitar ou rejeitar pedidos em ordem FIFO.

**Atualizar Status**
- Altera o status do pedido conforme o fluxo definido.

**Cancelar Pedido**
- Permitido apenas se o status for **AGUARDANDO APROVAÇÃO** ou **ACEITO**.

---

## 🔄 Fluxo de Filas

O sistema utiliza filas (**FIFO**) para organizar os pedidos:

- **Pendentes:** onde novos pedidos são inseridos.  
- **Aceitos:** pedidos aceitos seguem para o preparo (status **FAZENDO**).  
- **Prontos:** pedidos finalizados são movidos para esta fila (status **FEITO** → **ESPERANDO ENTREGADOR**).

---

## 🏷️ Status do Pedido

- AGUARDANDO APROVACAO  
- ACEITO  
- FAZENDO  
- FEITO  
- ESPERANDO ENTREGADOR  
- SAIU PARA ENTREGA  
- ENTREGUE  
- CANCELADO  
- REJEITADO  

---

## 🔍 Consultas Disponíveis
- Exibir todos os pedidos.  
- Filtrar pedidos por status.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**  
- Estruturas de dados nativas (`list`, `queue`)  
- Menu interativo no terminal  

---
