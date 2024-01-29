'''

Given a string str, the task is to find the longest substring which is a palindrome.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

•	Use two pointers, low and hi, for the left and right end of the current palindromic substring being found. 
•	Then checks if the characters at str[low] and str[hi] are the same. 
•	If they are, it expands the substring to the left and right by decrementing low and incrementing hi. 
•	It continues this process until the characters at str[low] and str[hi] are unequal or until the indices are in bounds.
•	If the length of the current palindromic substring becomes greater than the maximum length, it updates the maximum length.

Time complexity: O(N2), where N is the length of the input string
Space complexity: O(1), No extra space used.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        p1 = 0
        p2 = 0
        res = ""
        cnt = 0
        for i in range(n):

            # For even length
            p1, p2 = i, i+1
            while p1 >= 0 and p2 < n and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            if p2-p1-1 > cnt:
                res = ""
                for j in range(p1+1,p2):
                    res += s[j]
            cnt = max(cnt, p2-p1-1)
            print(res,cnt)

            # For odd length
            p1, p2 = i-1, i+1
            while p1 >= 0 and p2 < n and s[p1] == s[p2]:
                p1 -= 1
                p2 += 1
            if p2-p1-1 > cnt:
                res = ""
                for j in range(p1+1,p2):
                    res += s[j]
            cnt = max(cnt, p2-p1-1)
        return res


                

        

