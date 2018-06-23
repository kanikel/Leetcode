class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for (int i = s.length() - 1, j = 0; i >= 0;){
            result += (s[j] + 1 -'A') * pow(26,i);
            i--;
            j++;
            //cout << i << endl;
        }
        return result;
    }
};