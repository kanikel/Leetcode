import collections
import heapq as hq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # python的排序简直黑科技
        # time: O(n + klogn)
        # space: O(n) : store the count
        count = collections.Counter(words)
        heap = [[-val, word] for word, val in count.items()] # O(n)
        hq.heapify(heap)    # O(n)
        #r = [].append(hq.heappop(heap)[1] for _ in range(k)) # 这种写法会返回null，思考一下为什么，迭代的时候总是要[.. for .. in ..]把[]写在最外面
        r = [hq.heappop(heap)[1] for _ in range(k)] # O(logn) * k
        return r