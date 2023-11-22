import time

def selection_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0

    start_time = time.time()  # Marca o início do tempo de execução

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            comparacoes += 1
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        trocas += 1

    end_time = time.time()  # Marca o final do tempo de execução
    runtime = end_time - start_time

    return arr, trocas, comparacoes, runtime

# Criando uma lista em ordem decrescente
lista = list(range(99999, -1, -1))

sorted_list, trocas, comparacoes, tempo_execucao = selection_sort(lista.copy())

print(f"Quantidade de trocas: {trocas}")
print(f"Quantidade de comparações: {comparacoes}")
print(f"Tempo de execução: {tempo_execucao} segundos")