import time
import random
import matplotlib.pyplot as plt

# Fungsi Partition untuk pembagian elemen pivot
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Fungsi Quick Sort Iteratif
def quick_sort_iterative(arr):
    stack = []
    stack.append((0, len(arr) - 1))
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))

# Fungsi Quick Sort Rekursif
def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_recursive(less) + [pivot] + quick_sort_recursive(greater)

# Fungsi untuk membuat data skor pemain secara acak
def generate_random_scores(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Fungsi untuk mengukur waktu eksekusi
def measure_execution_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Ukuran data skor pemain yang akan diuji
input_sizes = [100, 500, 1000, 5000, 10000]
iterative_runtimes = []
recursive_runtimes = []

for size in input_sizes:
    scores = generate_random_scores(size)
    
    iterative_time = measure_execution_time(quick_sort_iterative, scores.copy())
    recursive_time = measure_execution_time(quick_sort_recursive, scores.copy())
    
    iterative_runtimes.append(iterative_time)
    recursive_runtimes.append(recursive_time)


#running time yang didapat
for i in range(len(input_sizes)):
    print(f"Running time iteratif untuk {input_sizes[i]} data: {iterative_runtimes[i]:.4f} detik")
    print(f"Running time rekursif untuk {input_sizes[i]} data: {recursive_runtimes[i]:.4f} detik")

# Visualisasi grafik perbandingan running time
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, iterative_runtimes, marker='o', label='Iterative')
plt.plot(input_sizes, recursive_runtimes, marker='s', label='Recursive')
plt.xlabel('Jumlah Data Skor Pemain')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Perbandingan Running Time Quick Sort Iteratif vs. Rekursif')
plt.legend()
plt.grid(True)
plt.show()
