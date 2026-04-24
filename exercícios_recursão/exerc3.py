def regressiva(n):
    print(n)
    if n > 0:
        regressiva(n - 1)

numero = int(input())
regressiva(numero)

#extra
def crescente(n):
    if n > 0:
        crescente(n - 1)
    print(n)

numero = int(input())
crescente(numero)