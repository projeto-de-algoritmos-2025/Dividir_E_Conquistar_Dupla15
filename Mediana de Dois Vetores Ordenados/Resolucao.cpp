#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // Função auxiliar: retorna a mediana de um pequeno grupo (até 5 elementos)
    int medianaGrupo(vector<int>& v, int inicio, int fim) {
        sort(v.begin() + inicio, v.begin() + fim + 1);
        int n = fim - inicio + 1;
        return v[inicio + n / 2];
    }

    // Função recursiva para encontrar o k-ésimo menor elemento (Mediana das Medianas)
    int kthSmallest(vector<int> v, int k) {
        int n = v.size();
        if (n <= 5) {
            sort(v.begin(), v.end());
            return v[k];
        }

        // Divide o vetor em grupos de 5 e pega a mediana de cada grupo
        vector<int> medianas;
        for (int i = 0; i < n; i += 5) {
            int fim = min(i + 4, n - 1);
            medianas.push_back(medianaGrupo(v, i, fim));
        }

        // Encontra a mediana das medianas recursivamente
        int mediana = kthSmallest(medianas, medianas.size() / 2);

        // Particiona o vetor em torno dessa mediana
        vector<int> menores, iguais, maiores;
        for (int x : v) {
            if (x < mediana) menores.push_back(x);
            else if (x == mediana) iguais.push_back(x);
            else maiores.push_back(x);
        }

        // Decide onde o k-ésimo menor está
        if (k < (int)menores.size())
            return kthSmallest(menores, k);
        else if (k < (int)(menores.size() + iguais.size()))
            return mediana;
        else
            return kthSmallest(maiores, k - menores.size() - iguais.size());
    }

    // Função principal: encontra a mediana de dois vetores ordenados
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged;
        merged.reserve(nums1.size() + nums2.size());
        merged.insert(merged.end(), nums1.begin(), nums1.end());
        merged.insert(merged.end(), nums2.begin(), nums2.end());

        int total = merged.size();
        if (total == 0) return 0.0;

        if (total % 2 == 1)
            return kthSmallest(merged, total / 2);
        else {
            int left = kthSmallest(merged, total / 2 - 1);
            int right = kthSmallest(merged, total / 2);
            return (left + right) / 2.0;
        }
    }
};
