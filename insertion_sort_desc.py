# insertion_sort_desc.py
"""
Assignment 1 - Insertion Sort (Decreasing Order)
MSCS 532
"""

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Compare with elements on the left and shift smaller ones
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    # Example array
    data = [5, 2, 9, 1, 5, 6]
    print("Original array:", data)
    sorted_data = insertion_sort_desc(data)
    print("Sorted array (decreasing):", sorted_data)
