'''

You are given a string 'str' and an integer ‘K’. Your task is to find the length of the largest substring with at most ‘K’ distinct characters.

For example:
You are given ‘str’ = ‘abbbbbbc’ and ‘K’ = 2, then the substrings that can be formed are [‘abbbbbb’, ‘bbbbbbc’]. Hence the answer is 7.

Sample Input 1:
2
2
abbbbbbc
3
abcddefg

Sample Output 1:
7
4
Explanation:
For the first test case, ‘str’ = ‘abbbbbbc’ and ‘K’ = 2, then the substrings that can be formed are [‘abbbbbb’, ‘bbbbbbc’]. Hence the answer is 7.

Approach
In this approach, we will make two pointers left and right. We start both pointers at 0 and increase the right pointer until we get more than K distinct characters between them. 
Then we will increase the left pointer until the number of distinct characters becomes less than or equal to K.
We repeat this process until both pointers reach the end of the string. We will update the answer as the maximum of answer and distance between both pointers in each step.

Time Complexity - O(N), Where N is the length of the string.
We are iterating the left and the right pointers over the string once, which will take O(N) time. All operations of HashMap will take O(1) time. Hence the overall time complexity is O(N).

Space Complexity - O(1).
We are maintaining a HashMap that will contain at most 26 different characters. Hence the overall space complexity is O(1).

'''

def kDistinctChars(k, s):
    # Write your code here
    # Return an integer value
    res = 0
    left = 0
    hashSet = {}
    n = len(s)
    for right in range(n):
        
        # Add the right most character of the string in the  map
        hashSet[s[right]] = hashSet.get(s[right], 0) + 1
        while left < right and len(hashSet) > k:
            # If the set has move than k unique characters then start decreasing the window from left
            hashSet[s[left]] -= 1
            
            # Remove the character from the map if it becomes 0
            if hashSet[s[left]] == 0:
                del hashSet[s[left]]
            left += 1
        res = max(res, right - left + 1)

    return res
