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
[ ]的closed interval的***left,right*** 值改變為***mid+1 or mid-1***  
[ )的open interval的***left,right*** 值改變為***mid***  

---------------------------------------------------



