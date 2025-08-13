
times = ["Flamengo", "Palmeiras", "Barcelona", "Santos", "Grêmio"]

tres_primeiros = times[:3]
print("3 primeiros colocados:", tres_primeiros)

ultimos_dois = times[-2:]
print("Últimos 2 colocados:", ultimos_dois)

ordem_alfabetica = sorted(times)
print("Times em ordem alfabética:", ordem_alfabetica)

posicao_barcelona = times.index("Barcelona") + 1
print("Posição do Barcelona:", posicao_barcelona)
