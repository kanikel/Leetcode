class Solution {
public:
    bool isPowerOfTwo(int n) {
        while (n != 1){
            int m = n % 2;
            if (m != 0 || n == 0)
                return false;
            n /= 2;
        }
        if (n == 1)
            return true;
    }
};
