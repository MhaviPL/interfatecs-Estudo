def decodificar(mensagem):
    print(mensagem)
    if len(mensagem) > 1:
        decodificar(mensagem[1:])

texto = input()
decodificar(texto)