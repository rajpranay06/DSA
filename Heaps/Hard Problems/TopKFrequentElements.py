'''

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Approach 1 - Using HashMap

'''

class Solution:
    def topKFrequent(self, a: List[int], k: int) -> List[int]:
        topk = k
        counts = Counter(a)
        max_counts = max(counts.values())
        
        # Create a bucket with maxCount as length
        bucket = [[] for _ in range(max_counts + 1)]
        
        # Add the key to its count index
        for k, v in counts.items():
            bucket[v].append(k)

        res = []
        # We can say the max count key are present from back of the bucket
        for i in range(len(bucket)-1, -1 ,-1):
            if len(bucket[i]) > 0:
                res += bucket[i]
                if len(res) >= topk:
                    break

        return res


'''

Approach 2 - Using Heap

'''

class Solution:
    def topKFrequent(self, a: List[int], k: int) -> List[int]:
        topk = k
        counts = Counter(a)
        
        res = []
        heap = []
        # Add key value pair to maxHeap
        for key, value in counts.items():
            heapq.heappush(heap, (-value, key))
        
        # Get top K values from maxHeap
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
