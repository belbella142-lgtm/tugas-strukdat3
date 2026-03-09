def bubbleSort(arr):
    n = len(arr)
    sorted_list = arr.copy()

    total_comparisons = 0
    total_swaps = 0
    passes_used = 0

    for i in range(n):
        swapped = False
        passes_used += 1

        for j in range(0, n - i - 1):
            total_comparisons += 1

            if sorted_list[j] > sorted_list[j + 1]:
                # swap
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                total_swaps += 1
                swapped = True

        # cetak array setelah setiap pass
        print(f"Pass {passes_used}: {sorted_list}")

        # early termination jika tidak ada swap
        if not swapped:
            break

    return (sorted_list, total_comparisons, total_swaps, passes_used)


# Uji dengan input yang diminta
data1 = [5, 1, 4, 2, 8]
data2 = [1, 2, 3, 4, 5]

print("Hasil data1:", bubbleSort(data1))
print()
print("Hasil data2:", bubbleSort(data2))