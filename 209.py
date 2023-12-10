class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            a = 0
            b = a+i
            while b <= len(nums):
                val = sum(nums[a:b])
                if val >= target:
                    return i 
                else:
                    a += 1
                    b += 1 
        return 0



