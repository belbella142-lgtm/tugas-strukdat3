# tugas-strukdat3

## Praktikum Data Structures & Algorithms
Program ini berisi implementasi beberapa algoritma pencarian dan pengurutan menggunakan bahasa Python.

# Soal 1 — Modified Binary Search
Fungsi `countOccurrences(sortedList, target)` digunakan untuk menghitung berapa kali suatu nilai muncul pada sebuah **sorted list**.
Algoritma menggunakan dua kali **binary search**:

1. Binary search pertama untuk menemukan **kemunculan pertama**.
2. Binary search kedua untuk menemukan **kemunculan terakhir**.

Jumlah kemunculan dihitung dengan rumus:

```
jumlah = right_index - left_index + 1
```

Kompleksitas waktu:

```
O(log n)
```

---

# Soal 2 — Bubble Sort dengan Analisis
Bubble sort dimodifikasi agar:

Menghitung jumlah **comparisons**
Menghitung jumlah **swaps**
Menghitung jumlah **passes**
Menggunakan **early termination** (berhenti jika tidak ada swap)

Contoh:

Input:

```
[5,1,4,2,8]
```

Output menunjukkan proses setiap pass hingga array menjadi terurut.

Jika array sudah terurut seperti:

```
[1,2,3,4,5]
```

maka algoritma akan berhenti lebih cepat karena tidak ada pertukaran.

# Soal 3 — Hybrid Sort

Hybrid Sort menggabungkan dua algoritma sorting:

* **Insertion Sort** untuk array kecil
* **Selection Sort** untuk array besar

Parameter:

```
threshold = 10
```

Jika panjang array lebih kecil dari threshold maka menggunakan insertion sort.

Tujuan hybrid sort adalah meningkatkan efisiensi dengan memilih algoritma yang lebih cocok berdasarkan ukuran data.

# Soal 4 — Merge Tiga Sorted Lists

Fungsi:

```
mergeThreeSortedLists(listA, listB, listC)
```

digunakan untuk menggabungkan tiga sorted list menjadi satu list yang tetap terurut.

Algoritma menggunakan **tiga pointer**:

```
i → listA
j → listB
k → listC
```

Setiap langkah memilih nilai terkecil dari ketiga list.

Kompleksitas waktu:

```
O(n)
```

di mana n adalah jumlah total elemen.

# Soal 5 — Inversion Counter

Inversion adalah pasangan indeks `(i, j)` dimana:

```
i < j tetapi arr[i] > arr[j]
```

Contoh:

```
[5,3,2]
```

Inversion:

```
(5,3)
(5,2)
(3,2)
```

Total = 3

Program menyediakan dua metode:

### 1. Naive Method

Menggunakan brute force:

```
O(n²)
```

dengan membandingkan setiap pasangan elemen.

### 2. Smart Method (Merge Sort)

Menggunakan modifikasi **merge sort**.

Saat proses merge, jika elemen kanan lebih kecil dari kiri, maka terjadi inversi sebanyak:

```
jumlah elemen sisa di left array
```

Kompleksitas waktu:

```
O(n log n)
```

Metode ini jauh lebih cepat untuk data besar.

# Cara Menjalankan Program

Jalankan dengan:

```
python praktikum_algoritma.py
```

Output akan menampilkan hasil pengujian dari setiap soal.
