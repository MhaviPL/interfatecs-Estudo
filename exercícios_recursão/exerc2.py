def somar_vetor(lista):
    if not lista:
        return 0
    return lista[0] + somar_vetor(lista[1:])

entrada = [4, 7, 2, 9]
resultado = somar_vetor(entrada)
print(resultado)