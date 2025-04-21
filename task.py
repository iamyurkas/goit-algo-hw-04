import random
import timeit
import sys

# Add recursia
sys.setrecursionlimit(10000)

# Insertion Sort
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result

# Timsort
def timsort(arr):
    return sorted(arr)

# Generate random data
def generate_data(size):
    return [random.randint(0, size) for _ in range(size)]

# Measure time
def benchmark():
    sizes = [100, 500, 1000, 2000]
    results = []

    for size in sizes:
        data = generate_data(size)
        print(f"\n🔍 Test {size}-elements array...")

        t_insertion = timeit.timeit(lambda: insertion_sort(data), number=1)
        t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
        t_tim = timeit.timeit(lambda: timsort(data), number=1)

        results.append((size, t_insertion, t_merge, t_tim))

        print(f"Insertion Sort: {t_insertion:.6f} с")
        print(f"Merge Sort:     {t_merge:.6f} с")
        print(f"Timsort:        {t_tim:.6f} с")

    return results

if __name__ == "__main__":
    benchmark()