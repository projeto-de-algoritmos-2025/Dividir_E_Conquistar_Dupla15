# Problema 3193: Contagem de Permutações por Inversões

!!! quote "Enunciado do Problema"
    Você recebe um inteiro `n` e uma matriz 2D `requirements`, onde `requirements[i] = [endi, cnti]` representa o índice final e a contagem de inversões de cada requisito.

    Um par de índices `(i, j)` de um array de inteiros `nums` é chamado de **inversão** se:
    * `i < j` e `nums[i] > nums[j]`

    Retorne o número de **permutações** `perm` de `[0, 1, 2, ..., n - 1]` tais que, para **todos** os `requirements[i]`, o prefixo `perm[0..endi]` tenha exatamente `cnti` inversões.

    Como a resposta pode ser muito grande, retorne-a **módulo** `$10^9 + 7$`.

---

!!! example "Exemplo 1"
    * **Entrada:** `n = 3`, `requirements = [[2,2],[0,0]]`
    * **Saída:** `2`
    * **Explicação:**
        As duas permutações são:
        1.  `[2, 0, 1]`
            * Prefixo `[2, 0, 1]` (índice 2) tem 2 inversões: (0, 1) e (0, 2).
            * Prefixo `[2]` (índice 0) tem 0 inversões.
        2.  `[1, 2, 0]`
            * Prefixo `[1, 2, 0]` (índice 2) tem 2 inversões: (0, 2) e (1, 2).
            * Prefixo `[1]` (índice 0) tem 0 inversões.

!!! example "Exemplo 2"
    * **Entrada:** `n = 3`, `requirements = [[2,2],[1,1],[0,0]]`
    * **Saída:** `1`
    * **Explicação:**
        A única permutação satisfatória é `[2, 0, 1]`:
        * Prefixo `[2, 0, 1]` (índice 2) tem 2 inversões: (0, 1) e (0, 2).
        * Prefixo `[2, 0]` (índice 1) tem 1 inversão: (0, 1).
        * Prefixo `[2]` (índice 0) tem 0 inversões.

!!! example "Exemplo 3"
    * **Entrada:** `n = 2`, `requirements = [[0,0],[1,0]]`
    * **Saída:** `1`
    * **Explicação:**
        A única permutação satisfatória é `[0, 1]`:
        * Prefixo `[0]` (índice 0) tem 0 inversões.
        * Prefixo `[0, 1]` (índice 1) tem 0 inversões.

---

!!! abstract "Restrições"
    * `2 <= n <= 300`
    * `1 <= requirements.length <= n`
    * `requirements[i] = [endi, cnti]`
    * `0 <= endi <= n - 1`
    * `0 <= cnti <= 400`
    * A entrada é gerada tal que existe pelo menos um `i` onde `endi == n - 1`.
    * A entrada é gerada tal que todos os `endi` são únicos.