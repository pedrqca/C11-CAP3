loja_do_pepe = {"Samsung", "Xiaomi", "Apple", "Motorola", "LG"}

loja_da_du = {"Samsung", "Xiaomi", "VivoPhone", "Peposmart", "XingLing"}

todos_modelos = loja_do_pepe | loja_da_du
print("Todos os modelos disponíveis:", todos_modelos)

iguais_modelos = loja_do_pepe & loja_da_du
print("Modelos iguais nas duas lojas:", iguais_modelos)