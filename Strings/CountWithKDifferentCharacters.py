'''

You are given a string 'str' of lowercase alphabets and an integer 'k' .

Your task is to return the count all the possible substrings that have exactly 'k' distinct characters.

For example:

'str' = abcad and 'k' = 2. 

We can see that the substrings {ab, bc, ca, ad} are the only substrings with 2 distinct characters. 

Therefore, the answer will be 4. 

Sample Input 1 :
aacfssa    
3
Sample Output 1 :
5    
Explanation of The Sample Input 1:
Given 'str' = “aacfssa”. We can see that the substrings with only 3 distinct characters are {aacf, acf, cfs, cfss, fssa}. 

The idea is to count all the subarrays with at most K distinct characters and then subtract all the subarrays with atmost K – 1 characters. 
That leaves us with count of subarrays with exactly K distinct characters.

'''

def most_k_chars(s, k):
    if not s:
        return 0
    char_count = {}
    num = 0
    left = 0
 
    for i in range(len(s)):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                char_count.pop(s[left])
            left += 1
        num += i - left + 1
    return num
def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    return most_k_chars(s, k) - most_k_chars(s, k - 1)

'''

Time Complexity: O(n)
Space Complexity: O(1)

'''

