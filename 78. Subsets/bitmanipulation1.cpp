class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        int size = nums.size();
        int maxi = 1 << size;
        
        for (int i = 0; i < maxi; i ++){
            vector<int> temp;
            for (int j = 0; j < size; j++){
                //cout << (1 << j) << " " << j << " " << ((1<<j) & i) <<endl;
                if (((1 << j) & i) != 0) //用了超级取巧的二进制计数加一的规律来遍历所有的组合，so fucking brilliant
                    res[i].push_back(nums[j]);}
            
        }
        return res;
        
        
    }
};
