import heapq

def ordenar_quase_ordenado(arr, k):
    n = len(arr)
    
    heap = arr[:k + 1]
    heapq.heapify(heap)
    
    indice_insercao = 0
    
    
    for i in range(k + 1, n):
        
        heapq.heappush(heap, arr[i])
        indice_insercao += 1
        
    
    while heap:
        arr[indice_insercao] = heapq.heappop(heap)
        indice_insercao += 1


vetor = [3, 2, 1, 5, 4, 7, 6]
ordenar_quase_ordenado(vetor, 3)
print(vetor)