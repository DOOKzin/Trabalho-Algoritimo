import time

def shell_sort(arr):
    trocas = 0
    comparacoes = 0

    start_time = time.time()  # Marca o início do tempo de execução

    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            comparacoes += 1
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                trocas += 1

            arr[j] = temp

        gap //= 2

    end_time = time.time()  # Marca o final do tempo de execução
    runtime = end_time - start_time

    return arr, trocas, comparacoes, runtime

# Criando uma lista ordenada de 0 a 999
lista_ordenada = list(range(10000))

sorted_list, trocas, comparacoes, tempo_execucao = shell_sort(lista_ordenada.copy())

print(f"Quantidade de trocas: {trocas}")
print(f"Quantidade de comparações: {comparacoes}")
print(f"Tempo de execução: {tempo_execucao} segundos")
