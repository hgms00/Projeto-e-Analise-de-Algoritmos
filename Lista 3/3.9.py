import math
def findMaximum(arr, mid):
    # Caso chegue em um ponto no qual arr[mid] é maior que ambos os elementos adjacente
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return arr[mid]
  
    # Se o arr[mid] é maior que o próximo elemento e menor que o elemento anterior
    if arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
        return findMaximum(arr, math.floor(mid/2))
    else: # Se o arr[mid] é menor que o próximo elemento e maior que o elemento anterior.
        return findMaximum(arr, math.floor((mid+len(arr)/2)-1))
  

arr = [1, 3, 10, 20, 30, 50, 60]
n = len(arr)
print ("O ponto máximo p é: %d"% findMaximum(arr, math.floor(n/2)))
 
