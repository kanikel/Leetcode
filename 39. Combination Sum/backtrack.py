class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def helper(r, cl, cs, ci):  # current result, current list, current sum, current index
            if cs == target:
                r.append(cl[:])
            for i in range(ci, len(candidates)):    # 一定要自己画出循环的结构才能理解递归的步骤，这里就是按大小顺序往下取
                if cs < target:
                    cl.append(candidates[i])
                    cs = sum(i for i in cl)
                    helper(r, cl, cs, i)
                    cl.pop()
        candidates.sort()
        r, cl = [], []
        helper(r, cl, 0, 0)
        return r