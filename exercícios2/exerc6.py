def quick_sort(vetor, inicio, fim):
    if inicio < fim:
        posicao_pivo = particao(vetor, inicio, fim)
        print(f"Pivô {vetor[posicao_pivo]} na posição {posicao_pivo}: {vetor}")
        quick_sort(vetor, inicio, posicao_pivo - 1)
        quick_sort(vetor, posicao_pivo + 1, fim)

def particao(vetor, inicio, fim):
    pivo = vetor[fim]
    i = inicio - 1
    
    for j in range(inicio, fim):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
            
    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1

lista = [10, 80, 30, 90, 40, 50, 70]
quick_sort(lista, 0, len(lista) - 1)
print("\nFinal:", lista)