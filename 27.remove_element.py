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

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fastindex, slowindex,nonval = 0, 0, 0
        for fastindex in range(len(nums)):
            if nums[fastindex] != val:
                nums[slowindex] = nums[fastindex]
                slowindex += 1               
        return slowindex       

