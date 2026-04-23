def recomendar(usuario, rede, visitados):
    if usuario not in visitados:
        print(usuario)
        visitados.add(usuario)
        
        for indicado in rede.get(usuario, []):
            recomendar(indicado, rede, visitados)

# Representação da rede social
conexoes = {
    "Renato": ["Ana", "Bruno"],
    "Ana": ["Carla"],
    "Bruno": ["Diego"],
    "Carla": [],
    "Diego": []
}

alcancados = set()
recomendar("Renato", conexoes, alcancados)

print("Total de usuários únicos:", len(alcancados))