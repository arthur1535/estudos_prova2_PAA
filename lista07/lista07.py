import math


# Questao 1: Minimo e Maximo Simultaneos
def min_max(v):
    n = len(v)
    if n == 0:
        return None, None, 0
    comparacoes = 0
    if n % 2 != 0:
        min_val = max_val = v[0]
        i = 1
    else:
        comparacoes += 1
        if v[0] <= v[1]:
            min_val, max_val = v[0], v[1]
        else:
            min_val, max_val = v[1], v[0]
        i = 2
    while i + 1 < n:
        comparacoes += 1
        if v[i] <= v[i + 1]:
            menor, maior = v[i], v[i + 1]
        else:
            menor, maior = v[i + 1], v[i]
        comparacoes += 1
        if menor < min_val:
            min_val = menor
        comparacoes += 1
        if maior > max_val:
            max_val = maior
        i += 2
    return min_val, max_val, comparacoes


# Questao 2: Algoritmo SELECTION com pivo no primeiro elemento
def particiona_primeiro(v, p, r, passos=None):
    pivo = v[p]
    i = p
    for j in range(p + 1, r + 1):
        if v[j] <= pivo:
            i += 1
            v[i], v[j] = v[j], v[i]
    v[p], v[i] = v[i], v[p]
    if passos is not None:
        passos.append(
            f"Pivo {pivo} fixado na pos {i + 1}: {v[p:r + 1]} (vetor: {v})"
        )
    return i


def selection(v, p, r, i, passos=None):
    if p == r:
        if passos is not None:
            passos.append(f"Subvetor unitario na pos {p + 1}: valor {v[p]}")
        return v[p]
    q = particiona_primeiro(v, p, r, passos)
    k = q - p + 1
    if i == k:
        if passos is not None:
            passos.append(f"Encontrado: i={i} == k={k}, elemento = {v[q]}")
        return v[q]
    elif i < k:
        if passos is not None:
            passos.append(f"Recurso a esquerda: i={i} <= k-1={k - 1}")
        return selection(v, p, q - 1, i, passos)
    else:
        if passos is not None:
            passos.append(f"Recurso a direita: novo_i={i - k} (k={k})")
        return selection(v, q + 1, r, i - k, passos)


# Questao 3: Tres metodos para os i maiores elementos
def top_i_metodo_a(v, i):
    # Metodo A: ordenacao completa Theta(n lg n)
    ordenado = sorted(v)
    return ordenado[-i:]


def top_i_metodo_b(v, i):
    # Metodo B: Max-Heap com i extracoes Theta(n + i lg n)
    import heapq
    # heapq em python e min-heap; invertemos o sinal para max-heap
    h = [-x for x in v]
    heapq.heapify(h)
    maiores = [-heapq.heappop(h) for _ in range(i)]
    return sorted(maiores)


def top_i_metodo_c(v, i):
    # Metodo C: selecao linear + particao + ordenacao dos i elementos Theta(n + i lg i)
    n = len(v)
    ordem_k = n - i + 1
    copia = v[:]
    pivo = selection(copia, 0, n - 1, ordem_k)
    maiores = [x for x in v if x >= pivo]
    return sorted(maiores)[:i]


# Questao 4: QuickSort com pior caso Theta(n lg n) usando mediana
def mediana_das_medianas(v):
    if len(v) <= 5:
        return sorted(v)[len(v) // 2]
    subgrupos = [v[j:j + 5] for j in range(0, len(v), 5)]
    medianas = [sorted(grupo)[len(grupo) // 2] for grupo in subgrupos]
    return mediana_das_medianas(medianas)


def quicksort_linear_pivot(v):
    if len(v) <= 1:
        return v[:]
    m = mediana_das_medianas(v)
    menores = [x for x in v if x < m]
    iguais = [x for x in v if x == m]
    maiores = [x for x in v if x > m]
    return quicksort_linear_pivot(menores) + iguais + quicksort_linear_pivot(maiores)


# Questao 5: Selecao com sub-rotina caixa-preta de mediana
def mediana_caixa_preta(v):
    # Simula a sub-rotina caixa-preta O(n)
    return sorted(v)[len(v) // 2]


def selecao_caixa_preta(v, i):
    if len(v) == 1:
        return v[0]
    m = mediana_caixa_preta(v)
    menores = [x for x in v if x < m]
    iguais = [x for x in v if x == m]
    maiores = [x for x in v if x > m]
    k = len(menores)
    if i <= k:
        return selecao_caixa_preta(menores, i)
    elif i <= k + len(iguais):
        return m
    else:
        return selecao_caixa_preta(maiores, i - k - len(iguais))


if __name__ == "__main__":
    print("LISTA 7 - O PROBLEMA DA SELECAO\n")

    print("1) MINIMO E MAXIMO SIMULTANEOS")
    A1 = [12, 35, 8, 42, 17, 91, 3, 25, 76, 50]
    min_v, max_v, comp = min_max(A1)
    limite = 3 * (len(A1) // 2)
    print(f"Vetor: {A1}")
    print(f"Minimo: {min_v} | Maximo: {max_v}")
    print(f"Comparacoes realizadas: {comp} (limite 3*floor(n/2) = {limite})\n")

    print("2) ALGORITMO SELECTION")
    A2 = [1, 8, 7, 6, 5, 3, 2, 10, 9]
    passos = []
    resultado_k3 = selection(A2[:], 0, len(A2) - 1, 3, passos)
    print(f"Vetor original: {A2} | Procurando 3o menor (i=3)")
    print("\n".join(passos))
    print(f"Resultado final: {resultado_k3}\n")

    print("3) TRES METODOS PARA OS i MAIORES ELEMENTOS")
    A3 = [45, 12, 85, 32, 89, 39, 69, 44, 42, 1, 98]
    i_val = 4
    res_a = top_i_metodo_a(A3, i_val)
    res_b = top_i_metodo_b(A3, i_val)
    res_c = top_i_metodo_c(A3, i_val)
    print(f"Vetor: {A3} | i = {i_val}")
    print(f"Metodo A (Ordenacao total): {res_a}")
    print(f"Metodo B (Max-Heap):        {res_b}")
    print(f"Metodo C (Selecao linear):  {res_c}\n")

    print("4) QUICKSORT COM PIOR CASO Theta(n lg n)")
    A4 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ordenado_qs = quicksort_linear_pivot(A4)
    print(f"Entrada em ordem decrescente (pior caso comum): {A4}")
    print(f"Ordenado com pivo de mediana deterministica:   {ordenado_qs}\n")

    print("5) SELECAO LINEAR COM CAIXA-PRETA DE MEDIANA")
    A5 = [38, 27, 43, 3, 9, 82, 10]
    for pos in [1, 3, 4, 7]:
        elem = selecao_caixa_preta(A5, pos)
        print(f"{pos}o menor elemento de {A5}: {elem}")
