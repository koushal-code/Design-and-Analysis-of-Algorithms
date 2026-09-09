import java.util.Scanner;

public class FactorialIterative {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Taking input
        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        // Starting time
        long startTime = System.nanoTime();

        // Calculate factorial
        long factorial = 1;

        for (int i = 1; i <= n; i++) {
            factorial = factorial * i;
        }

        // Ending time
        long endTime = System.nanoTime();

        // Execution time
        long executionTime = endTime - startTime;

        // Output
        System.out.println("Factorial of " + n + " = " + factorial);
        System.out.println("Time Complexity: O(n)");
        System.out.println("Space Complexity: O(1)");
        System.out.println("Execution Time: " + executionTime + " nanoseconds");

        sc.close();
    }
}

