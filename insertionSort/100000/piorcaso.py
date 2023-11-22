import time

def insertion_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0

    start_time = time.time()  # Marca o início do tempo de execução

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        comparacoes += 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            trocas += 1

        arr[j + 1] = key

    end_time = time.time()  # Marca o final do tempo de execução
    runtime = end_time - start_time

    return arr, trocas, comparacoes, runtime

# Criando uma lista em ordem decrescente
lista = list(range(99999, -1, -1))

sorted_list, trocas, comparacoes, tempo_execucao = insertion_sort(lista.copy())

print(f"Quantidade de trocas: {trocas}")
print(f"Quantidade de comparações: {comparacoes}")
print(f"Tempo de execução: {tempo_execucao} segundos")
