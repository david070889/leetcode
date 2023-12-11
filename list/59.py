class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        insert = []
        for i in range(n):
            matrix.append([0]*n)
        i = 0
        j = n-1
        L = 0
        a = 0 #starting point
        for x in  range(n**2):
            insert.append(x+1)

        if n % 2 == 1:
            layer = int((n+1)/2)
            while i < layer - 1:    
                for q in range(L,j):
                    matrix[L][q] = insert[q-L]
                a += j-2*L
                for q in range(L,j):
                    matrix[q][j-L] = insert[a+q-L]
                a += j-2*L
                for q in range(j-L-1,L-1,-1):
                    matrix[j-L][q+1] = insert[a+j-1-q-L]
                a += j-2*L
                for q in range(j-L-1,L-1,-1):
                    matrix[q+1][L] = insert[a+j-1-q-L]
                a += j-2*L
                i += 1
                j -= 1
                L += 1
            if i == layer-1:
                matrix[layer-1][layer-1] = n**2
            

        else:
            layer = n / 2
            while i < layer:  
                for q in range(L,j):
                    matrix[L][q] = insert[q-L]
                a += j-2*L
                for q in range(L,j):
                    matrix[q][j-L] = insert[a+q-L]
                a += j-2*L
                for q in range(j-L-1,L-1,-1):
                    matrix[j-L][q+1] = insert[a+j-1-q-L]
                a += j-2*L
                for q in range(j-L-1,L-1,-1):
                    matrix[q+1][L] = insert[a+j-1-q-L]
                a += j-2*L
                i += 1
                j -= 2
                L += 1
        return matrix
        

