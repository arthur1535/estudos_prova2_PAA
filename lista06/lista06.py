import random


# Questao 1: Merge Sort
def merge_sort(v, inicio=1, passos=None):
    if len(v) <= 1:
        return v[:], 0
    meio = (len(v) + 1) // 2
    esq, c1 = merge_sort(v[:meio], inicio, passos)
    dir, c2 = merge_sort(v[meio:], inicio + meio, passos)
    resultado = []
    i = j = comparacoes = 0
    while i < len(esq) and j < len(dir):
        comparacoes += 1
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado += esq[i:] + dir[j:]
    if passos is not None:
        p, q, r = inicio, inicio + meio - 1, inicio + len(v) - 1
        passos.append(f"Merge({p},{q},{r}) -> {resultado} ({comparacoes} comp.)")
    return resultado, c1 + c2 + comparacoes


# Questao 2: Quick Sort com tres escolhas de pivo
def quick_sort(v, tipo, passos, sorteador=None):
    if len(v) <= 1:
        return v[:], 0
    if tipo == "primeiro":
        indice = 0
    elif tipo == "mediana":
        candidatos = [0, (len(v) - 1) // 2, len(v) - 1]
        indice = sorted(candidatos, key=lambda i: v[i])[1]
    else:
        indice = sorteador.randrange(len(v))
    pivo = v[indice]
    outros = v[:indice] + v[indice + 1:]
    esq = [x for x in outros if x <= pivo]
    dir = [x for x in outros if x > pivo]
    passos.append(f"{v} -> {esq} |{pivo}| {dir}")
    a, c1 = quick_sort(esq, tipo, passos, sorteador)
    b, c2 = quick_sort(dir, tipo, passos, sorteador)
    return a + [pivo] + b, len(outros) + c1 + c2


# Questao 3: particionamento de Lomuto
def lomuto(v, l, r, passos=None):
    pivo = v[r]
    i = l - 1
    for j in range(l, r):
        if v[j] <= pivo:
            i += 1
            v[i], v[j] = v[j], v[i]
        if passos is not None:
            passos.append(f"j={j + 1}, i={i + 1}, vetor={v}")
    v[i + 1], v[r] = v[r], v[i + 1]
    return i + 1


# Questao 4: merge de k vetores ordenados
def merge_duas(a, b):
    i = j = 0
    saida = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            saida.append(a[i])
            i += 1
        else:
            saida.append(b[j])
            j += 1
    return saida + a[i:] + b[j:]


def merge_k(vetores):
    if len(vetores) == 1:
        return vetores[0][:]
    meio = len(vetores) // 2
    return merge_duas(merge_k(vetores[:meio]), merge_k(vetores[meio:]))


# Questao 5: Quick-Find (Quickselect), k comeca em 1
def quick_find(v, k, sorteador):
    l, r = 0, len(v) - 1
    while l <= r:
        escolha = sorteador.randint(l, r)
        v[escolha], v[r] = v[r], v[escolha]
        q = lomuto(v, l, r)
        posicao = q - l + 1
        if k == posicao:
            return v[q]
        if k < posicao:
            r = q - 1
        else:
            l = q + 1
            k -= posicao


if __name__ == "__main__":
    print("LISTA 6 - DIVISAO E CONQUISTA\n")

    print("1) MERGE SORT")
    passos = []
    ordenado, comparacoes = merge_sort(list(range(1, 11)), passos=passos)
    print("\n".join(passos))
    print("Resultado:", ordenado, "| Comparacoes:", comparacoes, "\n")

    print("2) QUICK SORT")
    for tipo in ("primeiro", "mediana", "aleatorio"):
        passos = []
        ordenado, comparacoes = quick_sort(list(range(1, 11)), tipo, passos, random.Random(6))
        print(tipo + ":")
        print("\n".join(passos))
        print("Comparacoes:", comparacoes, "\n")

    print("3) PARTITION-LOMUTO")
    v = [4, 8, 2, 7, 6, 3, 5, 1, 9, 10]
    passos = []
    indice = lomuto(v, 0, len(v) - 1, passos)
    print("\n".join(passos))
    print("Pivo na posicao:", indice + 1, "| Vetor:", v, "\n")

    print("4) MERGE DE K VETORES")
    vetores = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("Entrada:", vetores)
    print("Resultado:", merge_k(vetores), "\n")

    print("5) QUICK-FIND")
    v = [4, 8, 2, 7, 6, 3, 5, 1, 9, 10]
    print("Vetor:", v, "| k=5")
    print("5o menor:", quick_find(v, 5, random.Random(6)))
