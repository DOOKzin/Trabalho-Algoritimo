import time

def quick_sort(arr):
    trocas = 0
    comparacoes = 0

    def partition(low, high):
        nonlocal trocas, comparacoes
        pivot_index = (low + high) // 2
        pivot = arr[pivot_index]

        # Move o pivô para o final
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        trocas += 1

        i = low - 1

        for j in range(low, high):
            comparacoes += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        trocas += 1

        return i + 1

    def quick_sort_recursive(low, high):
        nonlocal trocas, comparacoes
        if low < high:
            partition_index = partition(low, high)

            quick_sort_recursive(low, partition_index - 1)
            quick_sort_recursive(partition_index + 1, high)

    start_time = time.time()  # Marca o início do tempo de execução

    quick_sort_recursive(0, len(arr) - 1)

    end_time = time.time()  # Marca o final do tempo de execução
    runtime = end_time - start_time

    return arr, trocas, comparacoes, runtime

# Criando uma lista ordenada de 0 a 999
lista_ordenada = list(range(1000))

sorted_list, trocas, comparacoes, tempo_execucao = quick_sort(lista_ordenada.copy())

print(f"Quantidade de trocas: {trocas}")
print(f"Quantidade de comparações: {comparacoes}")
print(f"Tempo de execução: {tempo_execucao} segundos")
