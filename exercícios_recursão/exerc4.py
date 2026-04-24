def potencia(base, expoente):
    if expoente == 0:
        return 1
    
    if expoente < 0:
        return 1 / potencia(base, -expoente)
    
    return base * potencia(base, expoente - 1)

b = int(input())
e = int(input())
print(potencia(b, e))