def BubbleSort(array, reverse=False, callback=None):
    array = array.copy()
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if (not reverse and array[j] > array[j + 1]) or (
                reverse and array[j] < array[j + 1]
            ):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if callback:
            callback(int((i + 1) / n * 100))
        if not swapped:
            break
        if callback:
            callback(int((i + 1) / n * 100))
    return array


def InsertionSort(array, reverse=False, callback=None):
    array = array.copy()
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and (
            (not reverse and array[j] > key) or (reverse and array[j] < key)
        ):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        if callback:
            callback(int((i + 1) / n * 100))
    return array


def MergeSort(array, reverse=False, callback=None):
    array = array.copy()
    if len(array) > 1:
        mid = len(array) // 2
        left_half = MergeSort(array[:mid], reverse, callback)
        right_half = MergeSort(array[mid:], reverse, callback)

        array = merge(left_half, right_half, reverse)
        if callback:
            callback(int(len(array) / len(array) * 100))
    return array


def merge(left_half, right_half, reverse):
    merged_array = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if (not reverse and left_half[i] < right_half[j]) or (
            reverse and left_half[i] > right_half[j]
        ):
            merged_array.append(left_half[i])
            i += 1
        else:
            merged_array.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged_array.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged_array.append(right_half[j])
        j += 1

    return merged_array


def SelectionSort(array, reverse=False, callback=None):
    array = array.copy()
    n = len(array)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if (not reverse and array[j] < array[minimum]) or (
                reverse and array[j] > array[minimum]
            ):
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
        if callback:
            callback(int((i + 1) / n * 100))
    return array


def HybridMergeSort(array, reverse=False, callback=None):
    array = array.copy()
    if len(array) > 1:
        if len(array) < 16:
            array = InsertionSort(array, reverse)
        else:
            mid = len(array) // 2
            left_half = HybridMergeSort(array[:mid], reverse, callback)
            right_half = HybridMergeSort(array[mid:], reverse, callback)

            array = merge(left_half, right_half, reverse)
            if callback:
                callback(int(len(array) / len(array) * 100))
    return array


def QuickSort(A, reverse=False, callback=None):
    A = A.copy()
    p = 0
    r = len(A) - 1

    def quick_sort_recursive(A, p, r, reverse, callback):
        if p < r:
            q = Partition(A, p, r, reverse)
            quick_sort_recursive(A, p, q - 1, reverse, callback)
            quick_sort_recursive(A, q + 1, r, reverse, callback)
            if callback:
                callback(int((r - p + 1) / len(A) * 100))

    quick_sort_recursive(A, p, r, reverse, callback)
    return A


def Partition(A, p, r, reverse):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if (not reverse and A[j] <= x) or (reverse and A[j] >= x):
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def CountingSort(arr, reverse=False, callback=None):
    if not arr:
        return []
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1
    count = [0] * range_of_elements
    for num in arr:
        count[num - min_value] += 1
    if not reverse:
        for i in range(1, len(count)):
            count[i] += count[i - 1]
    else:
        for i in range(len(count) - 2, -1, -1):
            count[i] += count[i + 1]
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_value] - 1] = arr[i]
        count[arr[i] - min_value] -= 1
        if callback:
            callback(int((len(arr) - i) / len(arr) * 100))
    return output


def BucketSort(array, reverse=False, callback=None):
    if not array:
        return array

    num_buckets = len(array)
    max_value = max(array)
    min_value = min(array)
    bucket_range = (max_value - min_value) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in array:
        index_b = int((num - min_value) / bucket_range)
        if index_b == num_buckets:
            index_b -= 1
        buckets[index_b].append(num)

    for i in range(num_buckets):
        buckets[i] = InsertionSort(buckets[i], reverse, callback)

    sorted_array = []
    if reverse:
        for i in range(len(buckets) - 1, -1, -1):
            sorted_array.extend(buckets[i])
    else:
        for i in range(len(buckets)):
            sorted_array.extend(buckets[i])
        if callback:
            callback(int((i + 1) / num_buckets * 100))

    return sorted_array


def countingSortForRadix(arr, digit_place, reverse=False, callback=None):
    buckets = [[] for _ in range(10)]

    for number in arr:
        index = (number // digit_place) % 10
        if reverse:
            index = 9 - index
        buckets[index].append(number)

    sorted_array = []
    if reverse:
        for i in range(len(buckets) - 1, -1, -1):
            sorted_array.extend(buckets[i])
    else:
        for i in range(len(buckets)):
            sorted_array.extend(buckets[i])
        if callback:
            callback(int((digit_place) / 10 * 100))

    if callback:
        callback(int(digit_place / max(arr) * 100))

    return sorted_array


def RadixSort(arr, reverse=False, callback=None):
    if len(arr) == 0:
        return arr

    max_value = max(arr)

    digit_place = 1
    while max_value // digit_place > 0:
        arr = countingSortForRadix(arr, digit_place, reverse, callback)
        digit_place *= 10

    return arr if not reverse else arr[::-1]


def heapify(arr, n, i, reverse=False, callback=None):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and (
        (not reverse and arr[left] > arr[largest])
        or (reverse and arr[left] < arr[largest])
    ):
        largest = left

    if right < n and (
        (not reverse and arr[right] > arr[largest])
        or (reverse and arr[right] < arr[largest])
    ):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, reverse, callback)
        if callback:
            callback(int((i + 1) / n * 100))


def HeapSort(arr, reverse=False, callback=None):
    arr = arr.copy()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, reverse, callback)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, reverse, callback)
        if callback:
            callback(int((n - i) / n * 100))
    return arr


def ShellSort(arr, reverse=False, callback=None):
    arr = arr.copy()
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and (
                (not reverse and arr[j - gap] > temp)
                or (reverse and arr[j - gap] < temp)
            ):
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
            if callback:
                callback(int((i + 1) / n * 100))

        gap //= 2
        if callback:
            callback(int((n - gap) / n * 100))

    return arr
