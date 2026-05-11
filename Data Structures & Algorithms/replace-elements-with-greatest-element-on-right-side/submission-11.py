class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i])
        initial_max = -1

        for i in range(len(arr) -1, -1, -1):
            new_max = max(initial_max,arr[i])
            arr[i] = initial_max
            initial_max = new_max
    
        return arr
