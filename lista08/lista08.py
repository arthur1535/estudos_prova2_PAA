import itertools
import math


# Questao 1: Arvore de decisao otima para n = 4 elementos
def sort4(v, passos=None):
    """Ordena 4 elementos com no maximo 5 comparacoes (Ford-Johnson / Arvore Otima)."""
    x1, x2, x3, x4 = v
    comp = 0

    # 1a comparacao: x1 e x2
    comp += 1
    if x1 <= x2:
        # 2a comparacao: x3 e x4
        comp += 1
        if x3 <= x4:
            # 3a comparacao: x1 e x3
            comp += 1
            if x1 <= x3:
                # 4a comparacao: x2 e x4
                comp += 1
                if x2 <= x4:
                    # 5a comparacao: x2 e x3
                    comp += 1
                    res = [x1, x2, x3, x4] if x2 <= x3 else [x1, x3, x2, x4]
                else:
                    res = [x1, x3, x4, x2]
            else:
                comp += 1
                if x4 <= x2:
                    comp += 1
                    res = [x3, x4, x1, x2] if x4 <= x1 else [x3, x1, x4, x2]
                else:
                    res = [x3, x1, x2, x4]
        else:
            comp += 1
            if x1 <= x4:
                comp += 1
                if x2 <= x3:
                    comp += 1
                    res = [x1, x2, x4, x3] if x2 <= x4 else [x1, x4, x2, x3]
                else:
                    res = [x1, x4, x3, x2]
            else:
                comp += 1
                if x3 <= x2:
                    comp += 1
                    res = [x4, x3, x1, x2] if x3 <= x1 else [x4, x1, x3, x2]
                else:
                    res = [x4, x1, x2, x3]
    else:
        # Ramo simetrico x1 > x2
        comp += 1
        if x3 <= x4:
            comp += 1
            if x2 <= x3:
                comp += 1
                if x1 <= x4:
                    comp += 1
                    res = [x2, x1, x3, x4] if x1 <= x3 else [x2, x3, x1, x4]
                else:
                    res = [x2, x3, x4, x1]
            else:
                comp += 1
                if x4 <= x1:
                    comp += 1
                    res = [x3, x4, x2, x1] if x4 <= x2 else [x3, x2, x4, x1]
                else:
                    res = [x3, x2, x1, x4]
        else:
            comp += 1
            if x2 <= x4:
                comp += 1
                if x1 <= x3:
                    comp += 1
                    res = [x2, x1, x4, x3] if x1 <= x4 else [x2, x4, x1, x3]
                else:
                    res = [x2, x4, x3, x1]
            else:
                comp += 1
                if x3 <= x1:
                    comp += 1
                    res = [x4, x3, x2, x1] if x3 <= x2 else [x4, x2, x3, x1]
                else:
                    res = [x4, x2, x1, x3]

    if passos is not None:
        passos.append(f"{v} -> {res} ({comp} comparacoes)")
    return res, comp


# Questao 2: Verificacao da cota de 5 elementos e 6 comparacoes
def verificar_picareta():
    n = 5
    comparam_alegadas = 6
    perm_possiveis = math.factorial(n)
    folhas_max = 2 ** comparam_alegadas
    cota_minima = math.ceil(math.log2(perm_possiveis))
    return {
        "n": n,
        "perm": perm_possiveis,
        "folhas": folhas_max,
        "cota_minima": cota_minima,
        "picareta": folhas_max < perm_possiveis
    }


# Questao 3: Counting Sort com rastreamento estavel
def counting_sort(A, k=4, passos=None):
    n = len(A)
    C = [0] * (k + 1)
    B = [0] * n

    # 1. Contagem de frequencias
    for x in A:
        C[x] += 1
    freq = list(C)

    # 2. Somas acumuladas (prefix sums)
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    acumulado = list(C)

    # 3. Alocacao reversa para garantir estabilidade
    for j in range(n - 1, -1, -1):
        val = A[j]
        pos = C[val] - 1  # 0-indexed
        B[pos] = val
        C[val] -= 1
        if passos is not None:
            passos.append(f"j={j + 1:2d}, A[j]={val} -> B[{pos + 1:2d}], C={C}")

    return B, freq, acumulado


# Questao 4: Radix Sort (LSD e MSD)
def radix_sort_lsd(A, d=3):
    """Radix Sort LSD (Least Significant Digit primeiro) com Counting Sort estavel."""
    arr = list(A)
    passadas = []
    exp = 1
    for p in range(1, d + 1):
        # Counting sort estavel pelo digito (x // exp) % 10
        C = [0] * 10
        B = [0] * len(arr)
        for x in arr:
            d_val = (x // exp) % 10
            C[d_val] += 1
        for i in range(1, 10):
            C[i] += C[i - 1]
        for j in range(len(arr) - 1, -1, -1):
            x = arr[j]
            d_val = (x // exp) % 10
            B[C[d_val] - 1] = x
            C[d_val] -= 1
        arr = B
        passadas.append(f"Passada {p} (exp={exp:3d}): {arr}")
        exp *= 10
    return arr, passadas


def radix_sort_msd(A, d_pos=2):
    """Radix Sort MSD (Most Significant Digit primeiro) recursivo por baldes."""
    if len(A) <= 1 or d_pos < 0:
        return A
    exp = 10 ** d_pos
    baldes = [[] for _ in range(10)]
    for x in A:
        d_val = (x // exp) % 10
        baldes[d_val].append(x)
    resultado = []
    for b in baldes:
        if len(b) > 0:
            resultado.extend(radix_sort_msd(b, d_pos - 1))
    return resultado


# Questao 5: Comparacao de complexidade Radix Sort vs Merge Sort
def simular_radix_merge(n_values):
    resultados = []
    for n in n_values:
        # Merge Sort: n * log2(n)
        custo_merge = n * math.log2(n)
        # Radix Sort bit a bit: k = 2, d = log2(n) -> d * (n + k)
        d_bit = math.ceil(math.log2(n))
        custo_radix_bit = d_bit * (n + 2)
        # Radix Sort agrupado: k = n, d = 1 -> 1 * (n + n) = 2n
        custo_radix_opt = 2 * n
        resultados.append((n, round(custo_merge), round(custo_radix_bit), round(custo_radix_opt)))
    return resultados


if __name__ == "__main__":
    print("LISTA 8 - ORDENACAO EM TEMPO LINEAR\n")

    print("1) ARVORE DE DECISAO (n = 4 elementos)")
    passos = []
    teste = [3, 1, 4, 2]
    res, comp = sort4(teste, passos)
    print("Entrada teste:", teste)
    print("\n".join(passos))
    # Validando todas as 24 permutacoes
    todas_permutacoes = list(itertools.permutations([1, 2, 3, 4]))
    todas_corretas = all(sort4(p)[0] == [1, 2, 3, 4] for p in todas_permutacoes)
    max_comp = max(sort4(p)[1] for p in todas_permutacoes)
    print(f"Total de permutacoes testadas: {len(todas_permutacoes)} | Todas corretas: {todas_corretas}")
    print(f"Numero de folhas l = {len(todas_permutacoes)} | Altura maxima h = {max_comp}\n")

    print("2) COTA DE 5 ELEMENTOS E O PROFESSOR PICARETA")
    q2 = verificar_picareta()
    print(f"Permutacoes possiveis (5!): {q2['perm']}")
    print(f"Folhas maximas com 6 comparacoes (2^6): {q2['folhas']}")
    print(f"Cota minima necessaria ceil(log2(120)): {q2['cota_minima']} comparacoes")
    print(f"O professor e picareta? {'SIM' if q2['picareta'] else 'NAO'}\n")

    print("3) COUNTING SORT PASSO A PASSO")
    A = [2, 3, 3, 4, 1, 3, 0, 3, 1, 2, 2, 1, 2, 4, 3, 4, 4, 2]
    passos_cs = []
    B, freq, acumulado = counting_sort(A, k=4, passos=passos_cs)
    print("Entrada A:", A)
    print("Frequencias C:", freq)
    print("Acumulado C:", acumulado)
    print("Passo a passo (18 iteracoes reversas):")
    print("\n".join(passos_cs[:5]) + "\n... (omissao visual de passos intermediarios) ...\n" + "\n".join(passos_cs[-3:]))
    print("Resultado final B:", B, "\n")

    print("4) RADIX SORT (LSD e MSD)")
    A_radix = [329, 457, 657, 839, 436, 720, 355]
    res_lsd, passadas = radix_sort_lsd(A_radix, d=3)
    print("Entrada:", A_radix)
    print("LSD:")
    print("\n".join(passadas))
    res_msd = radix_sort_msd(A_radix, d_pos=2)
    print("MSD:", res_msd)
    print("Custo computacional: T(n) = Theta(d(n + k))\n")

    print("5) RADIX SORT vs MERGE SORT")
    tabela = simular_radix_merge([64, 256, 1024, 4096])
    print(f"{'n':>6} | {'Merge Sort (n log n)':>22} | {'Radix Bit-a-Bit (k=2)':>22} | {'Radix Base n (Linear)':>22}")
    for row in tabela:
        print(f"{row[0]:6d} | {row[1]:22d} | {row[2]:22d} | {row[3]:22d}")
