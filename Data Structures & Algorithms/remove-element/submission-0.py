class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rtr = []

        for num in nums:
            if num != val:
               rtr.append(num)
        
        for i in range(len(rtr)):
            nums[i] = rtr[i]

        return len(rtr)