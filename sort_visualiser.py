import matplotlib.pyplot as plt # type: ignore
import random

def visualize(arr, algo_name, step, bar_color='blue', print_to_console=False):
    """
    Updates the bar chart and optionally prints the current step to the console.
    """
    plt.clf()
    plt.bar(range(len(arr)), arr, color=bar_color)
    plt.title(f"{algo_name} - Step {step}")
    plt.pause(0.1)
    if print_to_console:
        print(f"{algo_name} Step {step}: {arr}")

def bubble_sort(arr, print_to_console=False):
    n = len(arr)
    step = 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            visualize(arr, "Bubble Sort", step, print_to_console=print_to_console)
            step += 1

def insertion_sort(arr, print_to_console=False):
    step = 1
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        visualize(arr, "Insertion Sort", step, print_to_console=print_to_console)
        step += 1

def merge_sort(arr, step=[1], print_to_console=False):
    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], step, print_to_console)
    right = merge_sort(arr[mid:], step, print_to_console)
    merged = merge(left, right)
    arr[:len(merged)] = merged
    visualize(arr, "Merge Sort", step[0], print_to_console=print_to_console)
    step[0] += 1
    return merged

def quick_sort(arr, low=0, high=None, step=[1], print_to_console=False):
    if high is None:
        high = len(arr) - 1

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(low, high)
        visualize(arr, "Quick Sort", step[0], print_to_console=print_to_console)
        step[0] += 1
        quick_sort(arr, low, pi - 1, step, print_to_console)
        quick_sort(arr, pi + 1, high, step, print_to_console)

if __name__ == "__main__":
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    print("Choose an algorithm:")
    for i, algo in enumerate(algorithms.keys(), 1):
        print(f"{i}. {algo}")
    choice = int(input("Enter the number of the algorithm: "))
    algo_name = list(algorithms.keys())[choice - 1]
    algo_func = algorithms[algo_name]

    size = int(input("Enter the number of elements: "))
    array = [random.randint(1, 100) for _ in range(size)]
    print(f"Original Array: {array}")

    print_steps = input("Do you want to print the steps in the console as well? (yes/no): ").strip().lower() == "yes"

    plt.ion()
    fig = plt.figure()
    plt.title("Sorting Visualizer")

    algo_func(array, print_to_console=print_steps)
    plt.show(block=True)
    print(f"Sorted Array: {array}")
