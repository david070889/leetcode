class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [] #螺旋矩陣
        insert = [] #插入1-n^2數值的預備矩陣
        for i in range(n): #初始化matrix
            matrix.append([0]*n)
        i = 0 #控制while迴圈 iteration的次數
        j = n-1 #控制每次插入的個數 #控制插入的末端  #L|x|x|j n為5的矩陣，插入最外圈一次需要4個數字，L就是每次開始index j為每次結束的index(一圈分別為上下左右4次)
        L = 0 #現在處於得layer數 外->內為 0->layer-1 #控制插入的頭 
        a = 0 #starting point of insert list
        for x in  range(n**2): #將準備插入的1到n^2都在list中準備好
            insert.append(x+1)

        if n % 2 == 1: #n為odd
            layer = int((n+1)/2) #算出總共有幾層(中間的單個值也算一層)
            while i < layer - 1: #我們控制這裡的遞迴 只會到從外圈開始屬的倒數第二層 #雖然一開始一次插入j個，但是用range取範圍index只會到j-1，剛好符合
                for q in range(L,j): #從最外層的第一個開始 m(0,0) 到 m(0,j-1)
                    matrix[L][q] = insert[a+q-L] #insert[0:j-1]，插入j個 #L的部分解釋為，每向內移動一層，則填入數字的index區間就少一個
                a += n-1-2*L #每次插入後，加入插入的格數，使得下次帶入a即為當前插入開始的index #後面的L控制每向內一圈，則步數少了2
                for q in range(L,j): #最外層 m(0,j)到m(j-1,j)
                    matrix[q][j] = insert[a+q-L] 
                a += n-1-2*L
                for q in range(j,L,-1): #最外層 m(j,j)到m(j,1) #因為這邊matrix插入順序是右到左，所以range是大到小，造成insert這邊需要變成j-q才會是小到大
                    matrix[j][q] = insert[a+j-q]
                a += n-1-2*L
                for q in range(j,L,-1): #最外層 m(j,0)到m(1,0)
                    matrix[q][L] = insert[a+j-q]
                a += n-1-2*L
                i += 1
                j -= 1
                L += 1
            matrix[layer-1][layer-1] = n**2
            

        else : #n為even
            layer = int(n / 2) #算出總共有幾層
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
            matrix[layer-1][layer-1] = n**2
        else:
            layer = int(n / 2)
            matrix[layer-1][layer-1] = insert[n**2-4]
            matrix[layer-1][layer] = insert[n**2-3]
            matrix[layer][layer] = insert[n**2-2]
            matrix[layer][layer-1] = insert[n**2-1]
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

        return matrix
                
                
        

