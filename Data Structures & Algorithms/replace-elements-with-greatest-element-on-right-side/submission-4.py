class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k=[]
        
        for i in range(len(arr)):
            if i == len(arr) -1:
                k.append(-1)
            else: 
                k.append(max(arr[i+1:]))
        return k
