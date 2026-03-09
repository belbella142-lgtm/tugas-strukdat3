import random

def insertion_sort(a):
    c = s = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            c += 1
            a[j+1] = a[j]
            s += 1
            j -= 1
        a[j+1] = key
    return c + s

def selection_sort(a):
    c = s = 0
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            c += 1
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            s += 1
    return c + s

def hybridSort(a, threshold=10):
    if len(a) <= threshold:
        return insertion_sort(a.copy())
    else:
        return selection_sort(a.copy())

sizes = [50, 100, 500]

print("Ukuran | Hybrid | Insertion | Selection")
for n in sizes:
    data = [random.randint(1,1000) for _ in range(n)]
    print(n, "|", hybridSort(data), "|", insertion_sort(data.copy()), "|", selection_sort(data.copy()))