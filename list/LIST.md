# leetcode  
## 704. binary search  
range(stop)/range(5) => 0 1 2 3 4  
range(start,stop)/range(2,5) => 2 3 4  
range(start,stop,step)/range(1,10,2) => 1 3 5 7 9  

****

第二個後面用binary search 所寫  
因為是ascending且有固定區間(closed interval)  
比mid大在右半部，反之為左半部，等於mid則完成查找  
都沒有找到return -1  
[ ]的closed interval的***left,right*** 值改變為***mid+1,mid-1***  
[ )的open interval的***left,right*** 值改變為***mid+1,mid***  

---------------------------------------------------

## 27. remove element  
後面的code運用兩個index，第一個將每個都經過，第二個則是只有不能於想要移除的數值才移動  
所以第二個test 兩個index移動順序為 fast:01234567 slow:01xx234x  
這樣就將可以將後面不是val的值移動到val的位置並取代  
  
前面的code則是單純先找到出現val的次數 再一個個刪除  

***

## 977. Squares of a Sorted Array  
這題可以很直觀的暴力解出來，但根據使用的sorting method將會使時間複雜度為O(nlogn) or O(n^2)  
因為他是原始的array就是有序的，如果使用兩個index就可以很簡單的從左右兩側square往中間的數字從大排到小  
且只會有一次的遍歷array，所以為O(n)  
如果是從後面往前排，就變成小排到大  

***

## 209.Minimum Size Subarray Sum  
$\large\large\star \large\large\star \large\large\star$  
(回來重看)  
第一部份的code為將全部可能都找出來，結果就是會超時(O(n^2))   
第二部分設兩個index，將index內所有elements加總，並持續更新minlength，就可以找到最小的長度  

***

## 59.Spiral Matrix II  
$\large\large\star \large\large\star \large\large\star \large\large\star$  
解題思路為 matrix由外到內 且 將每個layer又分成4個部分 依序處理 向右 向下 向左 向上的數字填入  
我們又將n分為奇數、偶數，這樣能更好的減少需要思考的迴圈參數，因為n為odd、even的最內層分別為1個數字 和 4個數字  
不論奇數，偶數，外層的處理都是一樣的，所以能看到我將第一段code縮減為第二段code  

