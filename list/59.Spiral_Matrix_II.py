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
                    matrix[L][q] = insert[a+q-L]
                a += n-1-2*L
                for q in range(L,j):
                    matrix[q][j] = insert[a+q-L]
                a += n-1-2*L
                for q in range(j,L,-1):
                    matrix[j][q] = insert[a+j-q]
                a += n-1-2*L
                for q in range(j,L,-1):
                    matrix[q][L] = insert[a+j-q]
                a += n-1-2*L
                i += 1
                j -= 1
                L += 1
            matrix[layer-1][layer-1] = n**2
            

        else :
            layer = int(n / 2)
            while i < layer - 1:  
                for q in range(L,j):
                    matrix[L][q] = insert[a+q-L]
                a += n-1-2*L
                for q in range(L,j):
                    matrix[q][j] = insert[a+q-L]
                a += n-1-2*L
                for q in range(j,L,-1):
                    matrix[j][q] = insert[a+j-q]
                a += n-1-2*L
                for q in range(j,L,-1):
                    matrix[q][L] = insert[a+j-q]
                a += n-1-2*L
                i += 1
                j -= 1
                L += 1
            
            matrix[layer-1][layer-1] = insert[a]
            matrix[layer-1][layer] = insert[a+1]
            matrix[layer][layer] = insert[a+2]
            matrix[layer][layer-1] = insert[a+3]
        return matrix
                
        

