class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 if i not in count else count[i] + 1

        sortedCount = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        return list(sortedCount.keys())[:k]