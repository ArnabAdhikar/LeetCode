#include <vector>
#include <algorithm>

using namespace std;

bool isPrime(int n) {
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

class Solution {
public:
    int maximumPrimeDifference(vector<int>& nums) {
        vector<int> primeNums;
        for (int i = 0; i < nums.size(); i++)
        {
            if (isPrime(nums[i]))
                primeNums.push_back(i);
        }

        int maxPrime = *max_element(primeNums.begin(), primeNums.end());
        int minPrime = *min_element(primeNums.begin(), primeNums.end());

        return abs(maxPrime - minPrime);
    }
};