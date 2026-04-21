class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if (i == len(arr)-1):
                arr[i] = -1
                break
            else:
                big = 0
            
                for j in range(i+1, len(arr)):
                    big = max(big, arr[j])
            
                arr[i] = big

        return arr
