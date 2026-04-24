import heapq

def k_mais_frequentes(nums, k):
    
    contagem = {}
    for n in nums:
        contagem[n] = contagem.get(n, 0) + 1
    
    
    heap = []
    for num, freq in contagem.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
            
    
    resultado = []
    while heap:
        freq, num = heapq.heappop(heap)
        resultado.append((num, freq))
    
    return resultado[::-1]


numeros = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
k = 3
print(k_mais_frequentes(numeros, k))