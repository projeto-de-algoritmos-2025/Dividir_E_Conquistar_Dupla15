# 973. K Closest Points to Origin

Dado um array de `points` onde `points[i] = [xi, yi]` representa um ponto no plano **X-Y** e um inteiro `k`, retorne os `k` pontos mais próximos da origem `(0, 0)`.

A distância entre dois pontos no plano X-Y é a **distância Euclidiana** (ou seja, $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$).

Você pode retornar a resposta em **qualquer ordem**. A resposta é **garantidamente** **única** (exceto pela ordem em que está).

---

## Exemplos

### Exemplo 1:

```plaintext
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]