def heapify(arr: list[int], n: int, i: int) -> None:
    """Maintains the max-heap property for a subtree rooted at index i.
    
    n: Total size of the active heap
    i: Index of the current root node
    """
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: list[int]) -> list[int]:
    """Sorts an array in ascending order using the Max-Heap Sort algorithm."""
    n = len(arr)

    # Step 1: Build max-heap (rearrange array)
    # Start from last non-leaf node (n // 2 - 1) down to root (0)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one from max-heap
    for i in range(n - 1, 0, -1):
        # Move current root (maximum element) to the end of array
        arr[0], arr[i] = arr[i], arr[0]

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print(f"Original array: {data}")
    heap_sort(data)
    print(f"Sorted array:   {data}")
