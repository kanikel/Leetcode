class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        LinkedList<List<Integer>> res = new LinkedList<List<Integer>>();
        if (nums == null || nums.length == 0) return res;
        helper(nums, 0, res, new LinkedList<Integer>());
        return res;
    }
    public void helper(int[] nums, int curidx, List<List<Integer>> res, List<Integer> cur){ 
        if (curidx == nums.length){
            res.add(new LinkedList<Integer>(cur));
        }
        else{
            //保留原来的
            helper(nums, curidx + 1, res, cur);
            //加上下一个
            cur.add(nums[curidx]);
            helper(nums, curidx + 1, res, cur);
            cur.remove(cur.size() - 1);
        }
    }
}