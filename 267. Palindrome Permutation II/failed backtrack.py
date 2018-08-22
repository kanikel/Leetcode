class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # TLE
        def ispalindrome(cl):
            left = 0
            right = len(s) - 1 
            #if len(cl) == len(s):
            while right > left:
                if cl[left] != cl[right]:
                    return False
                right -= 1
                left += 1
            return True
                
        def helper(r, cl, used):
            if len(cl) == len(s):
                print cl
                if ispalindrome(cl):
                    r.append(cl[:])

            for i in range(0, len(s)):
                if i > 0 and s[i] == s[i-1] and used[i-1]: continue
                if not used[i]:
                    cl += s[i]
                    used[i] = True
                    helper(r, cl, used)
                    cl = cl[:-1]
                    used[i] = False

        r, cl = [], ""
        if len(s) == 0 or len(s) == 1:
            return [s]
        used = [False] * len(s)
        l = list(s)
        l.sort()
        s = "".join(l)
        helper(r, cl, used)
        return r