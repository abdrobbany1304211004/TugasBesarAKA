import timeit
import matplotlib.pyplot as plt

# Fungsi Partition untuk pembagian elemen pivot
def partition(arr, low, high):
    pivot = arr[high][1]
    i = low - 1
    for j in range(low, high):
        if arr[j][1] < pivot:
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


# Daftar pemain dan skor game
players = [("byne", 450), ("kaniee", 680), ("stinger", 110), ("yui", 300), ("bibo", 888), 
           ("kaniee", 1150), ("baubau", 770), ("miko", 798), ("blast", 500), ("baka", 90), 
           ("junkie", 320), ("demonix", 662), ("leon", 760), ("drago", 1052), ("phoenic", 1102), 
           ("chama", 1055), ("fubuchan", 999)]

# Salin data pemain untuk kedua pendekatan
players_iterative = players.copy()

# Ukur waktu eksekusi untuk pendekatan iteratif
execution_time = timeit.timeit(lambda: quick_sort_iterative(players_iterative), number=1000)
quick_sort_iterative(players_iterative)


# Tampilkan hasil pengurutan dan running time
print("Hasil Akhir Pengurutan Iteratif:")
for player in players_iterative:
    print(player[0], ":", player[1])

print("Running Time Iteratif:", execution_time)
print()


# Visualisasi grafik perbandingan running time
plt.bar(["Iterative"], [execution_time], color=['blue'])
plt.xlabel('Metode Pengurutan')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Perbandingan Running Time Quick Sort Iteratif')
plt.show()