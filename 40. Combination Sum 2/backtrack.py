class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(r, cl, ci, cs, used):
            if cs == target:
                r.append(cl[:])
            
            for i in range(ci, len(c)):
                # 用花花的话来解释，就是当前层只能使用一次，当前层使用过后，下一层假如相同就不能再次使用
                if i > ci and c[i] == c[i-1] and used[i-1]: continue  # 这里的限定条件一定不能多，i > 0 这句话被i>ci这句话的作用重复了，而 used[i-1]，之所以不加是因为可能i-1就算没用，但是只要c[i]=c[i-1]都要过滤掉，是因为再早之前可能该重复元素也被用过而且刚好和等于target，所以只能使用一次？着重看下第40题的视频
                if cs < target:
                    cl.append(c[i])
                    cs = sum(i for i in cl)
                    used[i] = True
                    helper(r, cl, i+1, cs, used)
                    cl.pop()
        
        r, cl = [], []
        c = candidates[:]
        c.sort()
        """
                for i in range(len(c)):
            if c[i] > target:
                c.remove(c[i])
        """

        used = [False] * len(c)
        helper(r, cl, 0, 0, used)
        return r
        