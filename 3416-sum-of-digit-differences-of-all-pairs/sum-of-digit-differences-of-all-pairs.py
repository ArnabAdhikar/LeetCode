class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        num_digits = len(str(nums[0]))
        n = len(nums)

        # Initialize an array of dictionaries to count digit frequencies at each position
        digit_counts = [defaultdict(int) for _ in range(num_digits)]

        # Populate the digit counts for each position
        for num in nums:
            num_str = str(num)
            for i, digit in enumerate(num_str):
                digit_counts[i][int(digit)] += 1

        total_sum = 0

        # Calculate the sum of digit differences
        for i in range(num_digits):
            for digit1 in range(10):
                count1 = digit_counts[i][digit1]
                for digit2 in range(10):
                    if digit1 != digit2:
                        count2 = digit_counts[i][digit2]
                        total_sum += count1 * count2
        # Each difference is counted twice, so divide by 2
        return total_sum // 2
