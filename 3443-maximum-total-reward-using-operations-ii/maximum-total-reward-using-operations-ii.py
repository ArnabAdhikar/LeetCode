class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        # at the beginning, the x is 0, we set the first bit of binary to indicate x is 0.
        x = 1
        for num in rewardValues:
            # for each reward, only the x < reward can be used
            # so we only keep the x < reward as validX
            validX = x & ((1 << num) - 1)

            # for each value in validX, we add num to it
            # for example, if we have x = 5 (binary 100000) and num = 6
            # then we will have new x = 11, whose binary = 10000000000
            # == (100000) << 6
            x |= validX << num
        # return the largest x as the result
        return x.bit_length() - 1
