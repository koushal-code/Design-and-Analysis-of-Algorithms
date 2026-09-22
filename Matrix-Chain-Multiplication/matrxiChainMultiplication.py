def matrix_chain_order(p: list[int]) -> tuple[int, list[list[int]]]:
    """Computes the minimum scalar multiplication cost and split table for matrix chain multiplication.
    
    p: Array where matrix A_i has dimensions p[i-1] x p[i]
    Returns: (min_cost, split_table)
    """
    n = len(p) - 1  # Number of matrices

    # m[i][j] stores the minimum scalar multiplications for A_i...A_j
    m = [[0] * (n + 1) for _ in range(n + 1)]
    
    # s[i][j] stores the optimal split index k
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # chain_len is the length of the sub-chain of matrices
    for chain_len in range(2, n + 1):
        for i in range(1, n - chain_len + 2):
            j = i + chain_len - 1
            m[i][j] = float('inf')

            # Try all possible split points k between i and j-1
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m[1][n], s


def get_optimal_parenthesization(s: list[list[int]], i: int, j: int) -> str:
    """Reconstructs the optimal parenthesization string from the split table s."""
    if i == j:
        return f"A{i}"
    
    k = s[i][j]
    left = get_optimal_parenthesization(s, i, k)
    right = get_optimal_parenthesization(s, k + 1, j)
    return f"({left} x {right})"


if __name__ == "__main__":
    # Dimensions: A1 (10x30), A2 (30x5), A3 (5x60)
    dimensions = [10, 30, 5, 60]

    min_cost, split_table = matrix_chain_order(dimensions)
    expression = get_optimal_parenthesization(split_table, 1, len(dimensions) - 1)

    print(f"Minimum Scalar Multiplications: {min_cost}")
    print(f"Optimal Parenthesization:       {expression}")
