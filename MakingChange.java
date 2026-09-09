import java.util.Scanner;

public class MakingChange {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of coins: ");
        int n = sc.nextInt();

        int[] coins = new int[n];

        System.out.println("Enter coin denominations:");
        for (int i = 0; i < n; i++) {
            coins[i] = sc.nextInt();
        }

        System.out.print("Enter amount: ");
        int amount = sc.nextInt();

        // Start execution time
        long startTime = System.nanoTime();

        // DP array
        int[] dp = new int[amount + 1];

        // Initialize DP array
        for (int i = 1; i <= amount; i++) {
            dp[i] = amount + 1;
        }

        // Base case
        dp[0] = 0;

        // Dynamic Programming
        for (int i = 1; i <= amount; i++) {

            for (int j = 0; j < n; j++) {

                if (coins[j] <= i) {

                    dp[i] = Math.min(
                            dp[i],
                            dp[i - coins[j]] + 1
                    );
                }
            }
        }

        // End execution time
        long endTime = System.nanoTime();

        // Display result
        if (dp[amount] == amount + 1) {
            System.out.println("\nAmount cannot be made.");
        } else {
            System.out.println("\nMinimum number of coins = " + dp[amount]);
        }

        // Execution time
        long executionTime = endTime - startTime;

        System.out.println("Execution Time = " + executionTime + " nanoseconds");

        // Complexity
        System.out.println("\n--- Complexity ---");
        System.out.println("Time Complexity  = O(n × amount)");
        System.out.println("Space Complexity = O(amount)");

        sc.close();
    }
}