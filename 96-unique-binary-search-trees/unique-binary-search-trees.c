int solve(int n, int* dp);

int numTrees(int n) {
    // Initialize dynamic programming array
    int* dp = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) {
        dp[i] = -1;
    }
    // Call the solve function and return the result
    int result = solve(n, dp);
    free(dp);
    return result;
}

int solve(int n, int* dp) {
    // Base case: If n is 0 or 1, return 1
    if (n <= 1)
        return 1;
    // If the result is already computed, return it
    if (dp[n] != -1) {
        return dp[n];
    }
    // Initialize answer variable
    int ans = 0;
    // Iterate through all possible roots
    for (int i = 1; i <= n; i++) {
        // Calculate the number of unique BSTs for left and right subtrees
        ans += solve(i - 1, dp) * solve(n - i, dp);
    }
    // Memoize the result and return
    dp[n] = ans;
    return dp[n];
}