
total_idade = 0
contador_mulheres_menor_20 = 0

n = int(input("Digite o número de pessoas: "))

for i in range(n):
    print(f"\nPessoa {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    total_idade += idade

    if sexo == 'F' and idade < 20:
        contador_mulheres_menor_20 += 1

media_idade = total_idade / n

print(f"\nMédia de idade do grupo: {media_idade:.2f} anos")
print(f"Quantidade de mulheres com menos de 20 anos: {contador_mulheres_menor_20}")
