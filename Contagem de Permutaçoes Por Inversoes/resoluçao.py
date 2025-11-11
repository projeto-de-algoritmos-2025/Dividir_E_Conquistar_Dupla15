class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7
        MAX_K = 400 # Limite de inversões dado pelo problema

        # 1. Mapa de requisitos para checagem rápida O(1)
        req_map = {end: cnt for end, cnt in requirements}

        # dp[i][j] = # de permutações do prefixo [0..i] com 'j' inversões
        #            que satisfazem todas as regras ATÉ 'i'.
        dp = [[0] * (MAX_K + 1) for _ in range(n)]

        # 2. Caso Base (i=0): Prefixo de tamanho 1
        # Um elemento sozinho sempre tem 0 inversões.
        if 0 in req_map and req_map[0] != 0:
            return 0  # Impossível se a regra para i=0 não for 0.
        dp[0][0] = 1 # 1 jeito de ter 0 inversões com 1 elemento.

        # 3. Construção da DP (i=1 até n-1)
        for i in range(1, n):
            # 'prefix_sum' otimiza a transição (janela deslizante)
            # A transição é: dp[i][j] = sum(dp[i-1][j-k]) para k em [0, i]
            # (Adicionar o (i+1)-ésimo elemento pode criar de 0 a 'i' novas inversões)
            prefix_sum = 0
            for j in range(MAX_K + 1):
                # Adiciona o próximo elemento à janela
                prefix_sum = (prefix_sum + dp[i-1][j]) % MOD
                
                # Remove o elemento que saiu da janela (k > i)
                if j > i:
                    prefix_sum = (prefix_sum - dp[i-1][j - i - 1] + MOD) % MOD
                
                dp[i][j] = prefix_sum

            # 4. Filtro: Aplicar a regra para o índice 'i'
            # Se existe uma regra para este prefixo, "zere" todas as
            # contagens de inversão 'j' que não batem com a regra.