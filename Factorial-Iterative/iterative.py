def factorial_iterative(num: int) -> int:
    """Calculates factorial using a loop.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


if __name__ == "__main__":
    num = int(input("Enter any number : "))
    try:
        output = factorial_iterative(num)
        print(f"Iterative Factorial of {num} = {output}")
    except ValueError as e:
        print(f"Error: {e}")

