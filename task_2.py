def binary_search(sorted_array, target):
    low, high = 0, len(sorted_array) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        if sorted_array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        iterations += 1

    return iterations, sorted_array[low] if low < len(sorted_array) else None


def main():
    sorted_array = [1.0, 2.5, 3.5, 5.0, 7.2, 10.8]
    target_value = 4.0

    iterations, upper_bound = binary_search(sorted_array, target_value)

    print(f"Кількість ітерацій: {iterations}")
    print(f"Верхня межа: {upper_bound}")


if __name__ == "__main__":
    main()
