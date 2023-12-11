class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        s = n**2
        i = 0
        j = 0
        h = 1
        k =[]
        for i in range(n):
            k.append([0]*n)
        while h <= s:
            while j < n:
                k[i][j] = h
                j += 1
                h += 1
            j -= 1 
            while j > i:
                k[i][j] = h
                i += 1
                h += 1
            i -= 1
            while j == i:
                k[i][j] = h
                j -= 1
                h += 1
            j += 1
            while i > j:
                k[i][j] = h
                i -= 1
                h += 1
            i += 1
        return k
        

