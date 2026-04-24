def ordenar_logs(logs):
    if len(logs) <= 1:
        return logs

    meio = len(logs) // 2
    esq = ordenar_logs(logs[:meio])
    dir = ordenar_logs(logs[meio:])

    return mesclar(esq, dir)

def mesclar(esq, dir):
    res = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            res.append(esq[i])
            i += 1
        else:
            res.append(dir[j])
            j += 1
    res.extend(esq[i:])
    res.extend(dir[j:])
    return res

logs_sistema = [
    "2026-04-24 10:00:05",
    "2026-04-23 22:15:00",
    "2026-04-24 08:30:10",
    "2026-04-24 10:00:01"
]

logs_ordenados = ordenar_logs(logs_sistema)
for log in logs_ordenados:
    print(log)