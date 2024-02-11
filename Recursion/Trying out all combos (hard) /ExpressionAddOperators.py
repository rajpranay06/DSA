'''

Given a string num that contains only digits and an integer target, 
return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.


Time Complexity - O(4^N * N)
Space Complexity - O(N)

'''

class Solution:
    def addOperators(self, s: str, k: int) -> List[str]:
        
        res = []

        def dfs(index, path, cur_sum, prev):

            if index == len(s):
                if cur_sum == k:
                    res.append("".join(path))
                    return
            
            for i in range(index, len(s)):
                cur_str = s[index:i+1]
                cur_num = int(cur_str)

                if index == 0:
                    # For first index just add the char to the path
                    dfs(i+1, [cur_str], cur_num, cur_num)
                
                else:
                    # For addition
                    dfs(i+1, path + ["+"] + [cur_str], cur_sum + cur_num, cur_num)
                    
                    # For Subtraction
                    dfs(i+1, path + ["-"] + [cur_str], cur_sum - cur_num, -cur_num)
                    
                    # For multiplication
                    # We are using prev parameter to do multiplication sum
                    # Multiplication needs to follow BODMAS for eg -> 1+2*3 => 1+6 => 7 not 3*3 => 9
                    # To get this we need to subtract prev from the cur_sum 
                    # for 1+2*3 prev is 2 cur_sum is 3 => 3-2 gives 1, the previous sum before adding 2
                    # next we multiply cur_sum * prev i.e 3*2 => 6 add the 1 to it => 6+1 => 7
                    dfs(i+1, path + ["*"] + [cur_str], cur_sum - prev + cur_num * prev, cur_num * prev)
                
                # Not con sidering trailing 0s like in 105 05 is not an integer should only consider 5 
                if s[index] == '0':
                    break
        
        dfs(0, [], 0, 0)
        return res


            
