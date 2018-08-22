class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        LinkedList<List<Integer>> res = new LinkedList<List<Integer>>();
        if(nums == null || nums.length == 0) return res;
        helper(nums, 0, res, new LinkedList<Integer>());
        return res;
    }
    public void helper(int[] nums, int curidx, List<List<Integer>> res, List<Integer> cur){ 
        //递归算法的套路
        res.add(new LinkedList<Integer>(cur));
        for (int idx = curidx; idx < nums.length; idx ++){
            cur.add(nums[idx]);
            //System.out.printf("%s; %s; %s%n", idx, res, cur);
            helper(nums, idx+1, res, cur);
            cur.remove(cur.size()-1);
        }
    }
}
//经典的递归算法，和回溯算法的区别在哪？
//回溯本身就是一种递归啊