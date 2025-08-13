
nomes = []
pesos = []

for i in range(3):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    peso = float(input(f"Digite o peso de {nome} (kg): "))
    nomes.append(nome)
    pesos.append(peso)

indice_mais_pesado = pesos.index(max(pesos))
indice_mais_leve = pesos.index(min(pesos))

print(f"\nA pessoa mais pesada é {nomes[indice_mais_pesado]} com {pesos[indice_mais_pesado]} kg.")
print(f"A pessoa mais leve é {nomes[indice_mais_leve]} com {pesos[indice_mais_leve]} kg.")
