import matplotlib.pyplot as plt
import timeit
import random

# Algoritma Quick Sort Iteratif
def quicksort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    stack = []
    stack.append((0, len(arr) - 1))
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = arr[high][1]
            i = low - 1
            for j in range(low, high):
                if arr[j][1] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            stack.append((low, i))
            stack.append((i + 2, high))
    
    return arr

# Algoritma Quick Sort Rekursif
def quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[random.randint(0, len(arr) - 1)][1]
    lesser = [x for x in arr if x[1] < pivot]
    equal = [x for x in arr if x[1] == pivot]
    greater = [x for x in arr if x[1] > pivot]
    
    return quicksort_recursive(lesser) + equal + quicksort_recursive(greater)

# List pemain dan skor
players = [("byne", 450), ("kaniee", 680), ("stinger", 110), ("yui", 300), ("bibo", 888),
           ("kaniee", 1150), ("baubau", 770), ("miko", 798), ("blast", 500), ("baka", 90),
           ("junkie", 320), ("demonix", 662), ("leon", 760), ("drago", 1052), ("phoenic", 1102),
           ("chama", 1055), ("fubuchan", 999)]

# Pengurutan skor dengan algoritma Quick Sort Iteratif
sorted_scores_iterative = quicksort_iterative(players.copy())
iterative_time = timeit.timeit(lambda: quicksort_iterative(players.copy()), number=1000)

# Pengurutan skor dengan algoritma Quick Sort Rekursif
sorted_scores_recursive = quicksort_recursive(players.copy())
recursive_time = timeit.timeit(lambda: quicksort_recursive(players.copy()), number=1000)

# Plotting running time
labels = ['Iterative', 'Recursive']
times = [iterative_time, recursive_time]

#tampilan hasil akhir pengurutan dan running time
print("Hasil pengurutan skor:")
print("Iterative:", sorted_scores_iterative)
print("Recursive:", sorted_scores_recursive)


print("Running Time Iteratif:", iterative_time)
print("Running Time Rekursif:", recursive_time)

#tampilan grafik perbandingan running time
plt.bar(labels, times, color=['blue', 'orange'])
plt.xlabel('Approach')
plt.ylabel('Running Time (s)')
plt.title('Running Time Comparison')
plt.show()

