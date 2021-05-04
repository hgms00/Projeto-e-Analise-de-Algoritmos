def busca_binaria(A, esquerda, direita, item):
    # 1. Caso base: o elemento não está presente. 
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Índice encontrado
    if meio == item:
        return A[meio] == meio
    # 3. Continuar busca
    elif meio > item:
        return busca_binaria(A, esquerda, meio - 1, item)
    else: # meio < item
        return busca_binaria(A, meio + 1, direita, item)

A = [0, 1, 2, 3, 4, 8, 15, 20]
i = 4
#print('a={:d}, b={:d}'.format(i,i))
print('Procurando no array...\nA[{:d}] = {:d}'.format(i,i),'\nResultado: ',busca_binaria(A, 0, len(A) - 1, i))