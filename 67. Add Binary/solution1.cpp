class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        string result = "";
        int l1 = a.length() - 1;
        int l2 = b.length() - 1;
        for (int i = 0; i < max(a.length(),b.length()); ++i){
            int tA = a.length() > i ? (a[l1]-'0') : 0; // add zeroes for the shorter string
            int tB = b.length() > i ? (b[l2]-'0') : 0;
            result = char((tA + tB + carry) % 2 + '0') + result;
            //sum.insert(sum.begin(), (tA + tB + carry) % 2);
            carry = (tA + tB + carry)/2;
            l1 -= 1;
            l2 -= 1;
        }
        if (carry == 1){
            result = "1" + result;
        }
        return result;
    }
};