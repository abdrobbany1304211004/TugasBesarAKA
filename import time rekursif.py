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

# Fungsi Quick Sort Rekursif
def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0][1]
        less = [x for x in arr[1:] if x[1] <= pivot]
        greater = [x for x in arr[1:] if x[1] > pivot]
        return quick_sort_recursive(less) + [(arr[0][0], arr[0][1])] + quick_sort_recursive(greater)

# Daftar pemain dan skor game
players = [("byne", 450), ("kaniee", 680), ("stinger", 110), ("yui", 300), ("bibo", 888), 
           ("kaniee", 1150), ("baubau", 770), ("miko", 798), ("blast", 500), ("baka", 90), 
           ("junkie", 320), ("demonix", 662), ("leon", 760), ("drago", 1052), ("phoenic", 1102), 
           ("chama", 1055), ("fubuchan", 999)]

# Salin data pemain untuk pendekatan rekursif
players_recursive = players.copy()

# Ukur waktu eksekusi untuk pendekatan rekursif
execution_time = timeit.timeit(lambda: quick_sort_recursive(players_recursive), number=1000)
sorted_players = quick_sort_recursive(players_recursive)


# Tampilkan hasil akhir pengurutan dan running time
print("Hasil Akhir Pengurutan:")
for player in sorted_players:
    print(player[0], ":", player[1])

print("Running Time Rekursif:", execution_time)

# Visualisasi grafik running time
plt.bar(["Recursive"], [execution_time], color='orange')
plt.xlabel('Metode Pengurutan')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Running Time Quick Sort dengan Pendekatan Rekursif')
plt.show()