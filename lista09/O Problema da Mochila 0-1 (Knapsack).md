O **Problema da Mochila 0-1 (Knapsack Problem)** com capacidade máxima $W = 10\text{ kg}$ possui uma pequena divergência na sua digitação dos pesos (`{6, 4, 3, 4, 2}` tem 5 números) em relação aos valores (`{30, 14, 16, 9}` tem 4 números).

Esse exemplo com os valores `{30, 14, 16, 9}` e capacidade `10` é o exemplo clássico do livro *Algorithms* (Dasgupta, Papadimitriou e Vazirani), onde os **4 itens oficiais** são:

* **Item 1:** Peso $w_1 = 6\text{ kg}$, Valor $v_1 = 30$
* **Item 2:** Peso $w_2 = 3\text{ kg}$, Valor $v_2 = 14$
* **Item 3:** Peso $w_3 = 4\text{ kg}$, Valor $v_3 = 16$
* **Item 4:** Peso $w_4 = 2\text{ kg}$, Valor $v_4 = 9$

*(Se na sua prova o vetor de pesos tiver realmente 5 elementos ou trocar o $3$ pelo $4$, a mecânica abaixo é idêntica — inclusive deixei uma observação de como fica com 5 itens logo abaixo).*

---

**1. Quantas subsequências (subconjuntos) podem se formar?**

Para $n$ itens, onde cada item tem 2 escolhas binárias (entrar ou não entrar na mochila), o total de subconjuntos possíveis é **$2^n$**:

* **Para $n = 4$ itens** ($w = \{6, 3, 4, 2\}$): Existem **$2^4 = 16$ subconjuntos** no total (incluindo a mochila vazia $\emptyset$). Desses 16, **11 subconjuntos são válidos** (têm peso total $\le 10\text{ kg}$).
* **Caso sejam $n = 5$ itens** ($w = \{6, 4, 3, 4, 2\}$): Existem **$2^5 = 32$ subconjuntos** no total, dos quais **19 subconjuntos** respeitam o limite de $10\text{ kg}$.

---

**2. Resolução por Indução preocupado SOMENTE com o Peso (Soma de Subconjuntos / Subset Sum)**

Quando ignoramos o valor e olhamos apenas para o peso, o problema de decisão/otimização por indução busca responder: *"É possível preencher uma capacidade $j$ usando os primeiros $i$ itens?"* (ou maximizar o peso sem passar de $10\text{ kg}$).

* **Hipótese de Indução (Caso Base e Passo Indutivo):**
* **Caso Base ($i = 0$):** Com $0$ itens, só conseguimos formar o peso $0$.
* **Passo Indutivo (Item $i$ com peso $w_i$):** Assumindo que já sabemos todos os pesos possíveis formados pelos primeiros $i-1$ itens ($S_{i-1}$), ao avaliar o item $i$, temos duas opções:
1. **Não incluir o item $i$:** Mantemos todos os pesos que já conseguíamos formar em $S_{i-1}$.
2. **Incluir o item $i$:** Somamos $w_i$ a todos os pesos de $S_{i-1}$, descartando os que ultrapassarem $W = 10\text{ kg}$.

$$S_i = S_{i-1} \cup \{p + w_i \mid p \in S_{i-1} \text{ e } p + w_i \le 10\}$$






* **Rastreamento Passo a Passo (Indução nos Pesos $\{6, 3, 4, 2\}$):**
1. **$S_0$ (Nenhum item):** $\{0\}$
2. **$S_1$ (Adiciona item de $6\text{ kg}$):** $\{0\} \cup \{0+6\} = \{0, 6\}$
3. **$S_2$ (Adiciona item de $3\text{ kg}$):** $\{0, 6\} \cup \{0+3, 6+3\} = \{0, 3, 6, 9\}$
4. **$S_3$ (Adiciona item de $4\text{ kg}$):** $\{0, 3, 6, 9\} \cup \{4, 7, \mathbf{10}, \cancel{13}\} = \{0, 3, 4, 6, 7, 9, \mathbf{10}\}$
5. **$S_4$ (Adiciona item de $2\text{ kg}$):** $\{0, 3, 4, 6, 7, 9, 10\} \cup \{2, 5, 6, 8, 9, \cancel{11}, \cancel{12}\} = \{0, 2, 3, 4, 5, 6, 7, 8, 9, \mathbf{10}\}$


* **Resultado apenas para o Peso:** O peso máximo possível é **$10\text{ kg}$** (cravado), que pode ser formado tanto pelos itens $\{6\text{ kg}, 4\text{ kg}\}$ quanto por $\{4\text{ kg}, 4\text{ kg}, 2\text{ kg}\}$ (se houvesse o segundo 4).

---

**3. Solução Completa do Problema (Peso + Valor via Programação Dinâmica Bottom-Up)**

Quando colocamos o **Valor** na equação, a recorrência indutiva da tabela $K[i, w]$ (maior valor usando os primeiros $i$ itens com capacidade $w$) passa a ser:


$$K[i, w] = \max\Big( K[i-1, w], \;\; K[i-1, w - w_i] + v_i \Big) \quad \text{se } w_i \le w$$

**Tabela de Programação Dinâmica $K[i, w]$**

| Item ($i$) \ Cap ($w$) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **0 (Base)** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **1 ($w_1=6, v_1=30$)** | 0 | 0 | 0 | 0 | 0 | 0 | 30 | 30 | 30 | 30 | 30 |
| **2 ($w_2=3, v_2=14$)** | 0 | 0 | 0 | 14 | 14 | 14 | 30 | 30 | 30 | 44 | 44 |
| **3 ($w_3=4, v_3=16$)** | 0 | 0 | 0 | 14 | 16 | 16 | 30 | 30 | 30 | 44 | **46** |
| **4 ($w_4=2, v_4=9$)** | 0 | 0 | 9 | 14 | 16 | 23 | 30 | 30 | 39 | 44 | **46** |

**Quais são os melhores itens (Solução Ótima Global)?**

* **Valor Máximo:** **$46$** (na célula $K[4, 10]$).
* **Melhores Itens Escolhidos:** **Item 1 ($6\text{ kg}$, valor $30$) + Item 3 ($4\text{ kg}$, valor $16$)**.
* **Peso Total:** $6 + 4 = 10\text{ kg}$.
* *Nota sobre o caso alternativo:* Mesmo que o Item 2 tivesse peso $4\text{ kg}$ (valor $14$) no lugar de $3\text{ kg}$, a combinação ótima continuaria sendo exata: Item 1 ($6\text{ kg}, 30$) + Item 3 ($4\text{ kg}, 16$) = **$46$**.

---

**4. Qual é o Custo Computacional?**

A análise de complexidade de algoritmos em prova exige diferenciar a força bruta da Programação Dinâmica:

1. **Por Força Bruta / Indução Ingênua (Testar todos os subconjuntos):**
* **Tempo:** **$O(2^n)$** (exponencial). Cada novo item dobra a árvore de decisão.
* **Espaço:** **$O(n)$** (altura da árvore de recursão).


2. **Por Programação Dinâmica (Bottom-Up na Tabela $n \times W$):**
* **Tempo:** **$O(n \cdot W)$**, onde $n$ é a quantidade de itens e $W$ é a capacidade máxima da mochila. No nosso exemplo, fazemos apenas $4 \times 10 = 40$ operações (tanto para o problema só de pesos quanto para o problema com valores).
* **Espaço:** **$O(n \cdot W)$** para guardar a matriz completa (ou otimizável para **$O(W)$** se você atualizar um único vetor de trás para frente).
* **Pegadinha clássica de prova (Complexidade Pseudo-Polinomial):** Em Ciência da Computação, $O(n \cdot W)$ não é considerado puramente polinomial, mas sim **pseudo-polinomial**, porque $W$ é o *valor numérico* da capacidade e não a quantidade de bits para representá-lo ($b = \log_2 W$). Se $W$ passar de $10$ para $10.000.000.000$, a tabela explode na memória, embora o número de itens $n$ continue sendo $4$.