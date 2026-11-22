class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} # value -> freq

        if k > len(nums):
            return []

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        arr = []
        for num, c in count.items():
            arr.append([c,num])
        arr.sort(reverse = True)

        return [num for _, num in arr[:k]]