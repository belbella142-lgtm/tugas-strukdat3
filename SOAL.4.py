def mergeThreeSortedLists(listA, listB, listC):
    i = j = k = 0
    result = []

    while i < len(listA) or j < len(listB) or k < len(listC):
        a = listA[i] if i < len(listA) else float('inf')
        b = listB[j] if j < len(listB) else float('inf')
        c = listC[k] if k < len(listC) else float('inf')

        m = min(a, b, c)

        if m == a:
            result.append(a)
            i += 1
        elif m == b:
            result.append(b)
            j += 1
        else:
            result.append(c)
            k += 1

    return result


# Contoh penggunaan
A = [1, 5, 9]
B = [2, 6, 10]
C = [3, 4, 7]

print(mergeThreeSortedLists(A, B, C))