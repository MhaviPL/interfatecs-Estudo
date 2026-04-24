vetor = [15, 3, 20, 8, 42, 2]
n = len(vetor)
trocas = 0

for i in range(n):
    indice_max = i
    for j in range(i + 1, n):
        if vetor[j] > vetor[indice_max]:
            indice_max = j
            
    if indice_max != i:
        vetor[i], vetor[indice_max] = vetor[indice_max], vetor[i]
        trocas += 1
    
    print(vetor)

print("Total de trocas:", trocas)