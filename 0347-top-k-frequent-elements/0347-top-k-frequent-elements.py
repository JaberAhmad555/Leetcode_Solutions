import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums
        count=Counter(nums)
        heap=[]
        for num,occurence in count.items():
            heapq.heappush(heap, (occurence,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
