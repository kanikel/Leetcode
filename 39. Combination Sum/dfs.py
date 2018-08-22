class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 这道题还是使用了组合的原理，因为你做过了排列，所以面对组合才有思路
        
        def helper(r, cl, target, ci):  # current result, current list, current sum, current index
            if target == 0:
                r.append(cl[:])
            for i in range(ci, len(candidates)):    # 一定要自己画出循环的结构才能理解递归的步骤，这里就是按大小顺序往下取
                if target > 0:
                    if target < candidates[i]: break    # 经过了一次强剪枝，导致运行速度加快很多
                    cl.append(candidates[i])
                    helper(r, cl, target - candidates[i], i)
                    cl.pop()
        candidates.sort()
        r, cl = [], []
        helper(r, cl, target, 0)
        return r