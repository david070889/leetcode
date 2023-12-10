class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        L = len(nums)
        for i in range(L):
            if nums[i] == val:
                j += 1
        
        for i in range(j):
            nums.remove(val)
            nums.append(0)
        k = len(nums)-j            
        return k
