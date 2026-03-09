import time, random

# a) Brute Force O(n^2)
def countNaive(arr):
    return sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] > arr[j])

# b) Merge Sort O(n log n)
def countSmart(arr):
    if len(arr) <= 1: return arr, 0
    mid = len(arr) // 2
    left, left_inv = countSmart(arr[:mid])
    right, right_inv = countSmart(arr[mid:])
    
    merged, inv, i, j = [], left_inv + right_inv, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
            inv += (len(left) - i) # Kunci efisiensi
    return merged + left[i:] + right[j:], inv

# Uji dan Ukur Waktu
for n in [1000, 5000, 10000]:
    arr = [random.randint(1, 10000) for _ in range(n)]
    
    start = time.time(); res1 = countNaive(arr); t1 = time.time() - start
    start = time.time(); _, res2 = countSmart(arr); t2 = time.time() - start
    
    print(f"Size: {n} | Naive: {t1:.4f}s | Smart: {t2:.4f}s | Match: {res1==res2}")