import collections
import heapq as hq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # 难点在于已经有了counter的值，但是counter是字典，没有按照value的值进行排序过，而且怎么取key出来也是一个问题
        # 下面这种解法的秒点在于先把key取出来，然后再按照-count[w]的顺序（大的在前面）先排一遍，再按照w自己（也就是谁首字母小）的顺序再排一遍
        # 最后输出前面的k个值
        # time: O(nlogn)(排序的空间复杂度), space: O(n)
        
        count = collections.Counter(words) #可以直接用 不用再 counter[word] += 1 for word in words
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w],w))
        return candidates[:k]