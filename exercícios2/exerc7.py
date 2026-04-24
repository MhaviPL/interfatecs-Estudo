jogadores = [
    {"nome": "Matheus", "pontos": 85},
    {"nome": "Ana", "pontos": 92},
    {"nome": "Bruno", "pontos": 85},
    {"nome": "Carla", "pontos": 92}
]

n = len(jogadores)

for i in range(n):
    for j in range(0, n - i - 1):
        trocar = False
        
        
        if jogadores[j]["pontos"] < jogadores[j + 1]["pontos"]:
            trocar = True
        
        
        elif jogadores[j]["pontos"] == jogadores[j + 1]["pontos"]:
            if jogadores[j]["nome"] > jogadores[j + 1]["nome"]:
                trocar = True
        
        if trocar:
            jogadores[j], jogadores[j + 1] = jogadores[j + 1], jogadores[j]

for jogador in jogadores:
    print(f"{jogador['nome']}: {jogador['pontos']}")