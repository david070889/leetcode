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

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0
        
        while right < L:
            cur_sum += nums[right]
            
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_len if min_len != float('inf') else 0



