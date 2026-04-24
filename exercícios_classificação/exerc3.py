palavras = ["Zebra", "abacaxi", "Manga", "banana", "Caju"]
n = len(palavras)

for i in range(1, n):
    chave = palavras[i]
    j = i - 1
    
    while j >= 0 and chave.lower() < palavras[j].lower():
        palavras[j + 1] = palavras[j]
        j -= 1
    
    palavras[j + 1] = chave

print(palavras)