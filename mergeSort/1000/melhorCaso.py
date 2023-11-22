import time

def merge_sort(arr):
    trocas = 0
    comparacoes = 0

    def merge(left, right):
        nonlocal trocas, comparacoes
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparacoes += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    start_time = time.time()

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left, left_trocas, left_comparacoes, _ = merge_sort(left)
        right, right_trocas, right_comparacoes, _ = merge_sort(right)

        trocas += left_trocas + right_trocas
        comparacoes += left_comparacoes + right_comparacoes

        arr = merge(left, right)

    end_time = time.time()
    runtime = end_time - start_time

    return arr, trocas, comparacoes, runtime

lista_ordenada = list(range(1000))

sorted_list, trocas, comparacoes, tempo_execucao = merge_sort(lista_ordenada.copy())

print(f"Quantidade de trocas: {trocas}")
print(f"Quantidade de comparações: {comparacoes}")
print(f"Tempo de execução: {tempo_execucao} segundos")
