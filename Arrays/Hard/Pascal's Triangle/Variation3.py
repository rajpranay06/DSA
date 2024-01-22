'''

Given the number of rows n. Print the first n rows of Pascal’s triangle.

In Pascal’s triangle, each number is the sum of the two numbers directly above it as shown in the figure below:

Algorithm / Intuition
Now, in the optimal approach of variation 2, we have learned how to generate a row in O(n) time complexity. So, in order to optimize the overall time complexity, we will be using that approach for every row. Thus the total time complexity will reduce.

Approach:
The steps are as follows:

First, we will run a loop(say row) from 1 to n.
Inside the loop, we will call a generateRow() function and add the returned list to our final answer. Inside the function we will do the following:
First, we will store the 1st element i.e. 1 manually.
After that, we will use a loop(say col) that runs from 1 to n-1. It will store the rest of the elements.
Inside the loop, we will use the specified formula to print the element. We will multiply the previous answer by (row-col) and then divide it by col itself.
Thus, the entire row will be stored and returned.
Finally, we will return the answer list.

'''

class Solution:
    def pascal(n):
        ans = [1]   #inserting the 1st element
        k = 1

        #calculate the rest of the elements:
        for i in range(1,n):
            k *= (n-i)
            k //= i
            ans.append(k)
        return ans
            
    def generate(self, n: int) -> List[List[int]]:
        res = []

        #store the entire pascal's triangle:
        for i in range(1,n+1):
            res.append(Solution.pascal(i))

        return res


'''

Time Complexity: O(n2), where n = number of rows(given).
Reason: We are generating a row for each single row. The number of rows is n. And generating an entire row takes O(n) time complexity.

Space Complexity: In this case, we are only using space to store the answer. That is why space complexity can still be considered as O(1).

'''
