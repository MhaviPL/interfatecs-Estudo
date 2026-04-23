def contar_caminhos(linha, coluna, n, m, bloqueios):
    if (linha, coluna) in bloqueios or linha >= n or coluna >= m:
        return 0
    
    if linha == n - 1 and coluna == m - 1:
        return 1
    
    caminhos_direita = contar_caminhos(linha, coluna + 1, n, m, bloqueios)
    caminhos_baixo = contar_caminhos(linha + 1, coluna, n, m, bloqueios)
    
    return caminhos_direita + caminhos_baixo

# Configurações: Grade 3x3 e uma casa bloqueada em (1,1)
linhas = 3
colunas = 3
casas_bloqueadas = [(1, 1)] 

resultado = contar_caminhos(0, 0, linhas, colunas, casas_bloqueadas)
print(resultado)