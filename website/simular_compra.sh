curl -X 'POST' \
  'http://localhost:8000/compras' \
  -H 'Content-Type: application/json' \
  -d '{
    "cliente": {
        "nome": "João da Silva",
        "email": "joao@email.com",
        "telefone": "11999999999",
        "endereco": "Rua Exemplo, 123"
    },
    "pedido": {
        "status_pedido": "Pendente",
        "valor_total": 3999.90
    },
    "itens_pedido": [
        {
            "id_produto": 1,
            "quantidade": 2,
            "preco_unitario": 1999.95
        }
    ],
    "pagamento": {
        "metodo_pagamento": "PIX",
        "status_pagamento": "Aprovado",
        "valor_pago": 3999.90
    },
    "entrega": {
        "status_entrega": "Aguardando envio",
        "transportadora": "Correios"
    },
    "cupom": "DESCONTO10"
}'