compras = {}

estoque = {
    "hortifruti": {
        "banana": {"quantidade": 150, "unidade": "kg", "preco": 4.99},
        "maçã": {"quantidade": 120, "unidade": "kg", "preco": 6.50},
        "tomate": {"quantidade": 80, "unidade": "kg", "preco": 7.99},
        "alface": {"quantidade": 60, "unidade": "unidade", "preco": 2.50},
        "batata": {"quantidade": 200, "unidade": "kg", "preco": 3.99},
    },
    "açougue": {
        "carne bovina": {"quantidade": 90, "unidade": "kg", "preco": 39.90},
        "frango": {"quantidade": 110, "unidade": "kg", "preco": 14.99},
        "linguiça": {"quantidade": 45, "unidade": "kg", "preco": 18.50},
    },
    "laticínios": {
        "leite integral": {"quantidade": 300, "unidade": "litro", "preco": 4.79},
        "queijo mussarela": {"quantidade": 70, "unidade": "kg", "preco": 32.90},
        "iogurte": {"quantidade": 150, "unidade": "unidade", "preco": 3.99},
        "manteiga": {"quantidade": 85, "unidade": "unidade", "preco": 8.99},
    },
    "mercearia": {
        "arroz": {"quantidade": 250, "unidade": "kg", "preco": 5.49},
        "feijão": {"quantidade": 180, "unidade": "kg", "preco": 7.99},
        "macarrão": {"quantidade": 200, "unidade": "unidade", "preco": 4.29},
        "óleo de soja": {"quantidade": 130, "unidade": "unidade", "preco": 6.99},
        "açúcar": {"quantidade": 160, "unidade": "kg", "preco": 4.19},
        "café": {"quantidade": 95, "unidade": "unidade", "preco": 12.99},
    },
    "bebidas": {
        "água mineral": {"quantidade": 400, "unidade": "unidade", "preco": 2.49},
        "refrigerante": {"quantidade": 220, "unidade": "unidade", "preco": 7.99},
        "suco": {"quantidade": 100, "unidade": "unidade", "preco": 8.49},
    },
    "limpeza": {
        "detergente": {"quantidade": 140, "unidade": "unidade", "preco": 2.99},
        "sabão em pó": {"quantidade": 90, "unidade": "unidade", "preco": 15.90},
        "papel higiênico": {"quantidade": 170, "unidade": "pacote", "preco": 19.90},
    }
}

while True:
    pergunta = input("O que você deseja? (comprar, estoque, pagar, sair) ").strip().lower()
    if pergunta == "estoque":
        print("Categorias disponíveis:")
        for categoria in estoque.keys():
            print(f"- {categoria.title()}")
    if pergunta == "sair":
        print("Obrigado por visitar o supermercado!")
        break
    if pergunta == "pagar":
        total = 0
        print("\nResumo da compra:")
        print(compras)
        for produto, quantidade in compras.items():
            for categoria, produtos in estoque.items():
                if produto in produtos:
                    preco_unitario = produtos[produto]["preco"]
                    subtotal = preco_unitario * quantidade
                    total += subtotal
                    print(f"Produto: {produto.title()}, Quantidade: {quantidade}, Preço unitário: R${preco_unitario:.2f}, Subtotal: R${subtotal:.2f}")
        print(f"\nTotal a pagar: R${total:.2f}")
        break
    if pergunta == "comprar":
        print("Produtos disponíveis:")
        for categoria, produtos in estoque.items():
            print(f"\nCategoria: {categoria.title()}")
            print("=" * 40)
            for produto, detalhes in produtos.items():
                print(f"Produto: {produto.title()}, Quantidade: {detalhes['quantidade']} {detalhes['unidade']}, Preço: R${detalhes['preco']:.2f}")
        while True:        
            compra_prod = input("\nQual/Quais produtos você deseja comprar? ").strip().lower()
            if compra_prod in [prod for cat, prods in estoque.items() for prod in prods]:
                quantidade = int(input("Qual a quantidade desejada? "))
                compras[compra_prod] = quantidade
            else:
                print("Produto não encontrado no estoque. Por favor, escolha um produto válido.")
            adicionar = input("Deseja adicionar mais produtos? (sim/não) ").strip().lower()
            print(f"Produtos comprados até agora: {compras}")
            if adicionar == "nao" or adicionar == "não":
                break


        