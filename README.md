# PROVA 2 -- Projeto e Análise de Algoritmos (PAA)
**Professor:** Felipe A. Louza  
**Aluno:** Arthur Pires Lopes (12221EEL001)  
**Instituição:** Universidade Federal de Uberlândia (UFU) / FEELT  

Este repositório centraliza todos os materiais de estudo, enunciados oficiais originais, resoluções formais em LaTeX (versões para entrega e versões comentadas para estudo), depuradores visuais interativos em HTML e o guia integrado de revisão para a **Prova 2**, abrangendo os conteúdos das **Listas 6, 7 e 8** e a resolução completa da **Lista 9** (Programação Dinâmica).

---

## 📁 Estrutura Modular Organizada do Diretório `prova2/`

```text
prova2/
├── README.md                            <-- Índice geral e documentação de apoio
├── resumo_prova2.pdf                    <-- GUIA INTEGRADO DE REVISÃO DA PROVA 2 (4 páginas modulares)
├── resumo_prova2.tex                    <-- Código-fonte LaTeX do resumo integrado
│
├── lista06/                             <-- MÓDULO 1: DIVISÃO E CONQUISTA
│   ├── aula06_divisao_e_conquista.pdf   <-- Slides oficiais da Aula 06 (197 slides)
│   ├── lista06.pdf                      <-- Enunciado oficial original da Lista 6
│   ├── lista06_entrega.tex / .pdf       <-- Resolução formal direta para entrega (9 páginas)
│   ├── lista06_estudo.tex  / .pdf       <-- Resolução estendida comentada para estudos (12 páginas)
│   └── resolucao_visual_lista6.html     <-- Simulador visual interativo local (Merge, Quick, Lomuto)
│
├── lista07/                             <-- MÓDULO 2: O PROBLEMA DA SELEÇÃO
│   ├── lista07.pdf                      <-- Enunciado oficial original da Lista 7
│   ├── lista07_entrega.tex / .pdf       <-- Resolução formal direta para entrega (8 páginas)
│   ├── lista07_estudo.tex  / .pdf       <-- Resolução estendida comentada para estudos (12 páginas)
│   └── resolucao_visual_lista7.html     <-- Simulador visual interativo local (MinMax, Selection, BFPRT)
│
├── lista08/                             <-- MÓDULO 3: ORDENAÇÃO LINEAR E COTAS INFERIORES
│   ├── lista08.pdf                      <-- Enunciado oficial original da Lista 8
│   ├── lista08_entrega.tex / .pdf       <-- Resolução formal direta para entrega (7 páginas)
│   ├── lista08_estudo.tex  / .pdf       <-- Resolução estendida comentada para estudos (10 páginas)
│   └── resolucao_visual_lista8.html     <-- Simulador visual interativo local (Counting, Radix, Árvores)
│
└── lista09/                             <-- MÓDULO 4: PROGRAMAÇÃO DINÂMICA
    ├── aula09.pdf                       <-- Slides oficiais da Aula 09 (241 slides)
    ├── lista09.pdf                      <-- Enunciado oficial original da Lista 9 (10 questões)
    ├── lista09_entrega.tex / .pdf       <-- Resolução formal direta para entrega (12 páginas)
    ├── lista09_estudo.tex  / .pdf       <-- Resolução estendida comentada para estudos (14 páginas)
    ├── resolucao_visual_lista9.html     <-- Painel integrado interativo das 10 questões
    ├── debugger_visual_knapsack_mochila.html               <-- Simulador interativo da Mochila 0-1
    ├── debugger_visual_lis_programa_o_din_mica.html        <-- Simulador interativo da LIS
    ├── debugger_visual_problema_do_troco_coin_change.html <-- Simulador interativo do Troco Mínimo
    └── O Problema da Mochila 0-1 (Knapsack).md            <-- Estudo teórico comparativo de indução e PD
```

---

## 🚀 Acesso Rápido aos Materiais

### Revisão Geral
* 📄 [Guia Integrado de Revisão (resumo_prova2.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/resumo_prova2.pdf)
* 📝 [Código-Fonte TeX da Revisão (resumo_prova2.tex)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/resumo_prova2.tex)

### Lista 06: Divisão e Conquista
* 📄 [Enunciado Oficial (lista06.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista06/lista06.pdf)
* 📊 [Slides da Aula 06 (aula06_divisao_e_conquista.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista06/aula06_divisao_e_conquista.pdf)
* 📑 [Resolução para Entrega (lista06_entrega.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista06/lista06_entrega.pdf) | [LaTeX](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista06/lista06_entrega.tex)
* 📘 [Resolução para Estudos (lista06_estudo.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista06/lista06_estudo.pdf) | [LaTeX](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista06/lista06_estudo.tex)
* 🌐 [Simulador Visual Interativo (resolucao_visual_lista6.html)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista06/resolucao_visual_lista6.html)

### Lista 07: O Problema da Seleção
* 📄 [Enunciado Oficial (lista07.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista07/lista07.pdf)
* 📑 [Resolução para Entrega (lista07_entrega.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista07/lista07_entrega.pdf) | [LaTeX](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista07/lista07_entrega.tex)
* 📘 [Resolução para Estudos (lista07_estudo.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista07/lista07_estudo.pdf) | [LaTeX](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista07/lista07_estudo.tex)
* 🌐 [Simulador Visual Interativo (resolucao_visual_lista7.html)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista07/resolucao_visual_lista7.html)

### Lista 08: Ordenação Linear e Cotas Inferiores
* 📄 [Enunciado Oficial (lista08.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista08/lista08.pdf)
* 📑 [Resolução para Entrega (lista08_entrega.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista08/lista08_entrega.pdf) | [LaTeX](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista08/lista08_entrega.tex)
* 📘 [Resolução para Estudos (lista08_estudo.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista08/lista08_estudo.pdf) | [LaTeX](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista08/lista08_estudo.tex)
* 🌐 [Simulador Visual Interativo (resolucao_visual_lista8.html)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista08/resolucao_visual_lista8.html)

### Lista 09: Programação Dinâmica
* 📄 [Enunciado Oficial (lista09.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/lista09.pdf)
* 📊 [Slides da Aula 09 (aula09.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/aula09.pdf)
* 📑 [Resolução para Entrega (lista09_entrega.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/lista09_entrega.pdf) | [LaTeX](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/lista09_entrega.tex)
* 📘 [Resolução para Estudos (lista09_estudo.pdf)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/lista09_estudo.pdf) | [LaTeX](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/lista09_estudo.tex)
* 🌐 [Simulador Visual Geral (resolucao_visual_lista9.html)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/resolucao_visual_lista9.html)
* 🕹️ [Debugger Interativo Mochila 0-1 (debugger_visual_knapsack_mochila.html)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/debugger_visual_knapsack_mochila.html)
* 🕹️ [Debugger Interativo LIS (debugger_visual_lis_programa_o_din_mica.html)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/debugger_visual_lis_programa_o_din_mica.html)
* 🕹️ [Debugger Interativo Troco (debugger_visual_problema_do_troco_coin_change.html)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/debugger_visual_problema_do_troco_coin_change.html)
* 📖 [Estudo Teórico Mochila (O Problema da Mochila 0-1.md)](file:///c:/Users/amand/OneDrive%20-%20Universidade%20Federal%20de%20Uberl%C3%A2ndia/2026/analise%20de%20algoritmo/prova2/lista09/O%20Problema%20da%20Mochila%200-1%20(Knapsack).md)

---

## 🎯 Conteúdos Auditados por Lista

### Lista 6: Divisão e Conquista
1. **Merge Sort:** Execução passo a passo em $A = \langle 1, 2, \dots, 10 \rangle$, árvore completa de recursão (19 chamadas, 19 comparações) e recorrência $T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n \lg n)$.
2. **Quick Sort e Escolha de Pivô:**
   - Pivô como 1º elemento: pior caso degenerado em vetor ordenado ($\Theta(n^2)$, 45 comparações).
   - Pivô como Mediana de Três: garante partição balanceada no centro ($\Theta(n \lg n)$).
   - Pivô Aleatório: tempo esperado $\mathbb{E}[T(n)] \in \Theta(n \lg n)$, imune à entrada do adversário ($\mathbb{P}(\text{pior caso}) \approx 0{,}014\%$).
3. **Particionamento de Lomuto:** Rastreamento completo para $A = \langle 4, 8, 2, 7, 6, 3, 5, 1, 9, 10 \rangle$, demonstração formal por Invariante de Laço (Inicialização, Manutenção, Término) e complexidade $\Theta(n)$ tempo / $\Theta(1)$ espaço in-place.
4. **Merge de $k$ vetores ordenados de tamanho $n$:** Algoritmo por Divisão e Conquista em $T(k) = 2T(k/2) + \Theta(nk) \implies \Theta(nk \lg k)$ via Caso 2 do Teorema Mestre e abordagem via Min-Heap de tamanho $k$ em $O(nk \lg k)$ tempo e $O(k)$ espaço.
5. **Quick-Find (Quickselect):** Seleção do $k$-ésimo menor elemento particionando e descartando metade dos dados; profundidade média de recursão $\Theta(\log n)$ e tempo total linear ótimo $\Theta(n)$ no caso médio (soma de PG decrescente).

---

### Lista 7: O Problema da Seleção
1. **Mínimo e Máximo Simultâneos:** Algoritmo por comparação aos pares atingindo no máximo $3\lfloor n/2 \rfloor$ comparações (economia de 25\% frente ao método ingênuo de $2n-2$).
2. **Execução do Algoritmo `SELECTION`:** Rastreamento completo das 5 chamadas para encontrar o 3º menor elemento em $A = \langle 1, 8, 7, 6, 5, 3, 2, 10, 9 \rangle$ com pivô no primeiro elemento, retornando o valor $3$.
3. **Comparação dos Três Métodos para os $i$ Maiores Elementos:**
   - (a) Ordenação Total: $\Theta(n \lg n)$.
   - (b) Max-Heap com $i$ extrações: $\Theta(n + i \lg n)$.
   - (c) Seleção Linear + Partição + Ordenação Parcial: $\Theta(n + i \lg i)$ (assintoticamente ótimo para todo $i$).
4. **QuickSort com Pior Caso Ótimo $\Theta(n \lg n)$:** Seleção da mediana exata usando a sub-rotina linear `SELECT` (BFPRT) em $\Theta(m)$ como pivô, forçando partições balanceadas $\le n/2$ e tempo $\Theta(n \lg n)$ no pior caso.
5. **Seleção Linear com Caixa-Preta de Mediana:** Algoritmo de seleção que utiliza uma sub-rotina caixa-preta de mediana em tempo linear, demonstrando $T(n) \le T(n/2) + \Theta(n) \implies \Theta(n)$ no pior caso pelo Teorema Mestre.

---

### Lista 8: Ordenação em Tempo Linear e Cotas Inferiores
1. **Cota Inferior por Comparações ($\Omega(n \log n)$):**
   - Modelo de Árvore de Decisão binária ($l \ge n! \implies 2^h \ge n! \implies h \ge \lceil \log_2(n!) \rceil$).
   - Para $n = 4$: $l = 24$ folhas e altura mínima ótima $h = 5$ (diagrama em TikZ com ramos canônicos).
2. **O "Professor Picareta":** Prova matemática formal de que é impossível ordenar 5 elementos com 6 comparações ($2^6 = 64 < 120 = 5!$; pelo Princípio da Casa dos Pombos, exige-se no mínimo $\lceil \log_2 120 \rceil = 7$ comparações).
3. **Counting Sort:** Rastreamento passo a passo em tabela com 18 iterações reversas para $A = \langle 2, 3, 3, 4, 1, 3, 0, 3, 1, 2, 2, 1, 2, 4, 3, 4, 4, 2 \rangle$, comprovando estabilidade e custo $\Theta(n + k)$.
4. **Radix Sort:**
   - (a) MSD (Most Significant Digit): Divisão e conquista particionando em baldes de centenas e recursando nas dezenas.
   - (b) LSD (Least Significant Digit): Três passadas estáveis iterativas (unidades, dezenas, centenas).
   - (c) Custo temporal $\Theta(d(n + k))$ e espacial $\Theta(n + k)$.
5. **Empate de Custo entre Radix Sort e Merge Sort:** Demonstração de que quando $d = \Theta(\log n)$ (ex.: chaves até $n^c$ em binário $k = 2$) e $k = O(1)$, o Radix Sort consome $\Theta(n \log n)$, empatando exatamente com o Merge Sort.

---

### Lista 9: Programação Dinâmica (10 Questões Resolvidas)
1. **Cut-Rod Bottom-Up:** Execução passo a passo para tamanhos 0 a 6 com vetor de preços dados.
2. **Cut-Rod com Reconstrução da Solução Ótima:** Pseudocódigo e rastreamento para retornar os pedaços cortados.
3. **LIS (Longest Increasing Subsequence):** Rastreamento passo a passo da LIS em $\Theta(n^2)$ para $S = \langle 5, 2, 8, 6, 3, 6, 9, 7 \rangle$.
4. **LIS com Reconstrução de Sequência:** Algoritmo que recupera os elementos da subsequência crescente máxima.
5. **Problema do Troco (Coin Change):** Rastreamento com $C = [1, 5, 8, 11]$ e $k = 13$, determinando número mínimo de moedas.
6. **Troco sem Repetição de Moedas:** Formulação tipo Subset-Sum / Mochila 0-1.
7. **Contagem de Maneiras Diferentes de Formar o Troco:** Formulação aditiva de contagem de combinações.
8. **Mochila 0-1 (Knapsack):** Rastreamento da tabela bidimensional $n \times W$ para 4 itens e capacidade 10.
9. **Mochila com Repetição (Unbounded Knapsack):** Recorrência unidimensional em tempo $O(n \cdot W)$.
10. **LCS (Longest Common Subsequence) com Reconstrução:** Algoritmo completo que retorna a subsequência comum de tamanho máximo.

---

## 🛠️ Instruções de Compilação

Todos os documentos `.tex` são 100% autônomos, configurados com codificação `UTF-8` e pré-ambulos completos e limpos. Podem ser compilados diretamente no Overleaf ou localmente com `pdflatex`:

```bash
# Compilar o Guia Integrado de Revisão (4 páginas)
pdflatex resumo_prova2.tex

# Compilar Listas de Entrega
pdflatex lista06/lista06_entrega.tex
pdflatex lista07/lista07_entrega.tex
pdflatex lista08/lista08_entrega.tex
pdflatex lista09/lista09_entrega.tex

# Compilar Listas de Estudo Comentadas
pdflatex lista06/lista06_estudo.tex
pdflatex lista07/lista07_estudo.tex
pdflatex lista08/lista08_estudo.tex
pdflatex lista09/lista09_estudo.tex
```
