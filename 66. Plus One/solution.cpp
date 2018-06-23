class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int l = digits.size()-1;
        for (int i = 0; i < digits.size(); i++){
            if (digits[l] == 9){
                digits[l] = 0;
                l -= 1;
                if (l < 0){
                    digits.insert(digits.begin(),1);
                    break;
                }
            }
            else{
                    digits[l] += 1;
                    break;
                }
            }
        return digits;
        }
};