class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            print(bin(n))
            if n & 1 == 1:
                cnt += 1
            n = n>>1
        return cnt
        # cnt = 0
        # i = 1
        # while i <= n:
        #     if n & i == i:
        #         cnt += 1
        #     i = i << 1
        # return cnt