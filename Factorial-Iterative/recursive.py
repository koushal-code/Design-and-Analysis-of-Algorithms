def factorial_recursive(n: int) -> int:
    """Calculates factorial using recursion.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n in (0, 1):
        return 1
    
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    num = int(input("Enter any number : "))
    try:
        output = factorial_recursive(num)
        print(f"Recursive Factorial of {num} = {output}")
    except ValueError as e:
        print(f"Error: {e}")
