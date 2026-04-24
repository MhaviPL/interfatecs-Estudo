def explorar(sala_atual, mapa, visitadas):
    if sala_atual in visitadas:
        return
    
    print(sala_atual)
    visitadas.add(sala_atual)
    
    for vizinha in mapa.get(sala_atual, []):
        explorar(vizinha, mapa, visitadas)

predio = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

visitadas = set()
explorar("A", predio, visitadas)