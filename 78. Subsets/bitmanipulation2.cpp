class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        int size = nums.size();
        int maxi = 1 << size;
        vector<vector<int>> res(maxi, vector<int>()); //就加多了这一句，runtime就从error -> 100%,why?是因为提前分配好内存就不用每次都根据大小再拓宽？
        
        for (int i = 0; i < maxi; i ++){
            vector<int> temp;
            for (int j = 0; j < size; j++){
                //cout << (1 << j) << " " << j << " " << ((1<<j) & i) <<endl;
                if (((1 << j) & i) != 0) //用了超级取巧的二进制计数加一的规律来遍历所有的组合，bit manipulation is so fucking brilliant!!
                    res[i].push_back(nums[j]);}}
        return res;
    }
};