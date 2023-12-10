#暴力法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = pow(nums[i],2)
        nums.sort()
        return nums

#O(n)的方法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a, b, c = 0, len(nums)-1, len(nums)-1
        k = [float('inf')]*len(nums)
        for i in range(b+1):
            if nums[a]**2 > nums[b]**2:
                k[c] = nums[a]**2
                a += 1
                c -= 1
            elif nums[a]**2 <= nums[b]**2:
                k[c] = nums[b]**2
                b -= 1
                c -= 1
        return k
