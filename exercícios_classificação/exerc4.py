import random

original = [random.randint(1, 1000) for _ in range(100)]
vetor_bubble = list(original)
vetor_insertion = list(original)

# Bubble Sort
operacoes_bubble = 0
n = len(vetor_bubble)
for i in range(n):
    for j in range(0, n - i - 1):
        operacoes_bubble += 1
        if vetor_bubble[j] > vetor_bubble[j + 1]:
            vetor_bubble[j], vetor_bubble[j + 1] = vetor_bubble[j + 1], vetor_bubble[j]
            operacoes_bubble += 1

# Insertion Sort
operacoes_insertion = 0
for i in range(1, len(vetor_insertion)):
    chave = vetor_insertion[i]
    j = i - 1
    operacoes_insertion += 1 
    while j >= 0 and chave < vetor_insertion[j]:
        vetor_insertion[j + 1] = vetor_insertion[j]
        j -= 1
        operacoes_insertion += 2 
    vetor_insertion[j + 1] = chave


print("Operações Bubble Sort:", operacoes_bubble)
print("Operações Insertion Sort:", operacoes_insertion)