import time

def bubble_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0

    start_time = time.time()  # Marca o início do tempo de execução

    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1

    end_time = time.time()  # Marca o final do tempo de execução
    runtime = end_time - start_time

    return arr, trocas, comparacoes, runtime

# Criando uma lista em ordem decrescente
lista = list(range(9999, -1, -1))

sorted_list, trocas, comparacoes, tempo_execucao = bubble_sort(lista.copy())

print(f"Quantidade de trocas: {trocas}")
print(f"Quantidade de comparações: {comparacoes}")
print(f"Tempo de execução: {tempo_execucao} segundos")