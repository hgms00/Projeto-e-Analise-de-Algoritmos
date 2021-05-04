
# Retorna o índice do elemento máximo do array
def max(array, n): 
    index = 0
    for i in range(0,n): 
        if array[i] > array[index]: 
            index = i 
    return index 
def ordenarPanquecas(array, n): 
    tamanho_atual = n 
    while tamanho_atual > 1: 
        index = max(array, tamanho_atual) 
        # Move o maior elemento para o final do array
        if index != tamanho_atual-1: 
            # Move o maior elemento para o começo do array
            reverter(array, index)
            #Move o maior elemento para o final
            reverter(array, tamanho_atual-1) 
        tamanho_atual -= 1
# Reverte o array
def reverter(array, i): 
    inicio = 0
    while inicio < i: 
        temp = array[inicio] 
        array[inicio] = array[i] 
        array[i] = temp 
        inicio += 1
        i -= 1

array = [23, 10, 20, 11, 12, 6, 7] 
ordenarPanquecas(array, len(array)); 
print ("Array ordenado: ", array) 
