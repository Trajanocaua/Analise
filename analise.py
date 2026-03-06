print("=== Análise de Dados Simples ===")

vendas = [150, 200, 50, 400, 320, 180, 90]

total_vendas = sum(vendas)
quantidade = len(vendas)
media = total_vendas / quantidade
maior_venda = max(vendas)
menor_venda = min(vendas)

print("Vendas:", vendas)
print("Total de vendas:", total_vendas)
print("Quantidade de vendas:", quantidade)
print("Média de vendas:", media)
print("Maior venda:", maior_venda)
print("Menor venda:", menor_venda)
