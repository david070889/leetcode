#暴力法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = pow(nums[i],2)
        nums.sort()
        return nums

#double index, O(n)的方法(共只經過n個index的array一次)
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

#範例答案(更好的運用所有變數)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2: # 左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1 # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
        return res
