'''

Problem statement
You have been given an integer 'N'. Your task is to generate and return all binary strings of length 'N' such that there are no consecutive 1's in the string.

A binary string is that string which contains only ‘0’ and ‘1’.

For Example:
Let ‘N'=3, hence the length of the binary string would be 3. 

We can have the following binary strings with no consecutive 1s:
000 001 010 100 101 

Sample Input 1:
4
Sample Output 1:
0000 0001 0010 0100 0101 1000 1001 1010 
Explanation of sample input 1:
For N = 4 we get the following Strings:

0000 0001 0010 0100 0101 1000 1001 1010 

Note that none of the strings has consecutive 1s. Also, note that they are in a lexicographically increasing order.

Approach:

We Generate all possible strings recursively by considering both adding a ‘1’ and a ‘0’ at every index.
if ‘1’ was added at the last index we only add a ‘0’ and look for all possible substrings.

'''

def helper(a,s,n):
    if len(s) == n:
        a.append(s)
        return
    
    if s[-1] == '1':
        helper(a,s+'0',n)
    
    else:
        helper(a,s+'0',n)
        helper(a,s+'1',n)

def generateString(N: int) -> List[str]:
    # write your code here
    ans = []
    helper(ans, '0', N)
    helper(ans, '1', N)

    return ans
