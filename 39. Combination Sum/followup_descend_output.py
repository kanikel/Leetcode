class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 这道题还是使用了组合的原理，因为你做过了排列，所以面对组合才有思路
        
        def helper(r, cl, target, ci, n, cn):  # current result, current list, current sum, current index
            if cn == n:
                if target == 0:
                    r.append(cl[:])
            for i in range(ci, len(candidates)):    # 一定要自己画出循环的结构才能理解递归的步骤，这里就是按大小顺序往下取
                if target > 0:
                    if target < candidates[i]: break    # 经过了一次强剪枝，导致运行速度加快很多
                    cl.append(candidates[i])
                    #cn += 1
                    helper(r, cl, target - candidates[i], i, n, cn+1)
                    cl.pop()
                    #cn -= 1
        candidates.sort()
        r, cl = [], []
        for n in range(target/candidates[0]+1, 0, -1): # 0, target/candidates[0]+1 假如是要升序或降序
            helper(r, cl, target, 0, n, 0)
        return r
                    