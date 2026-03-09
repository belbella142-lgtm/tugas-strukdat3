# Fungsi untuk mencari posisi pertama target
def findFirst(arr, target):
    left = 0
    right = len(arr) - 1
    first = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            first = mid
            right = mid - 1   # terus cari ke kiri
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first


# Fungsi untuk mencari posisi terakhir target
def findLast(arr, target):
    left = 0
    right = len(arr) - 1
    last = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            last = mid
            left = mid + 1    # terus cari ke kanan
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last


# Fungsi utama untuk menghitung jumlah kemunculan
def countOccurrences(sortedList, target):
    first = findFirst(sortedList, target)

    if first == -1:
        return 0

    last = findLast(sortedList, target)

    return last - first + 1


# Contoh penggunaan
data = [1, 2, 4, 4, 4, 4, 7, 9, 12]

print(countOccurrences(data, 4))  # Output: 4
print(countOccurrences(data, 5))  # Output: 0