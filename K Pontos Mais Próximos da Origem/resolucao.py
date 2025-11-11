import random
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Função auxiliar para calcular distância ao quadrado (evita raiz quadrada)
        def dist_quadrada(point):
            return point[0]**2 + point[1]**2

        # Função principal de "Dividir e Conquistar" (Quickselect)
        def encontrar_os_k(lista_pontos, k_necessarios):
            
            # 1. DIVIDIR
            # Escolhe um pivô aleatório para dividir a lista
            pivo = random.choice(lista_pontos)
            dist_pivo = dist_quadrada(pivo)
            
            # Listas para pontos mais próximos, iguais e mais longe que o pivô
            mais_proximos = []
            mesma_dist = []
            mais_longe = []
            
            # Particiona a lista com base na distância do pivô
            for point in lista_pontos:
                d = dist_quadrada(point)
                if d < dist_pivo:
                    mais_proximos.append(point)
                elif d == dist_pivo:
                    mesma_dist.append(point)
                else:
                    mais_longe.append(point)
            
            # 2. CONQUISTAR
            # Verifica em qual partição os 'k' pontos estão
            
            num_proximos = len(mais_proximos)
            num_meio = len(mesma_dist)
            
            # Caso 1: 'k' pontos estão todos na lista 'mais_proximos'
            if k_necessarios <= num_proximos:
                # Busca recursiva APENAS nessa lista
                return encontrar_os_k(mais_proximos, k_necessarios)
            
            # Caso 2: 'k' pontos incluem 'mais_proximos' e 'mesma_dist'
            elif k_necessarios <= num_proximos + num_meio:
                # Achamos! Retorna 'mais_proximos' e o que falta da 'mesma_dist'
                return mais_proximos + mesma_dist[:k_necessarios - num_proximos]
            
            # Caso 3: Precisamos de pontos da lista 'mais_longe'
            else:
                # Retorna os dois primeiros e busca o resto em 'mais_longe'
                pontos_restantes = k_necessarios - num_proximos - num_meio
                return mais_proximos + mesma_dist + encontrar_os_k(mais_longe, pontos_restantes)

        # Inicia o processo com a lista original
        return encontrar_os_k(points, k)