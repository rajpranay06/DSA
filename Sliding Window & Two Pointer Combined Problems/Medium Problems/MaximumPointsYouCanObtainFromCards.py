'''

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.


Approach:

The approach optimises the solution by using a sliding window technique. We start with a window of size ‘K’ and calculate the initial sum. 
Then, we simulate moving the window from the end of the row by removing one card and adding another card from the other end. 
This allows us to find the maximum score without generating all possible combinations.

Time Complexity - O(K), where ‘K’ is the number of cards to be taken.
The initial loop to calculate the sum of the first ‘K’ cards runs in O(K) time. The second loop iterates from ‘K’-1 to 0, performing constant-time operations in each iteration. 
Hence, it runs in O(K) time. Therefore, the overall time complexity of the algorithm is O(K).

Space Complexity - O(1)
The algorithm uses a constant amount of extra space for variables such as ‘sum’ and ‘ans’. Hence, the space complexity is O(1).

'''

class Solution:
    def maxScore(self, arr: List[int], K: int) -> int:
        max_score = 0

        # Calculate the initial score by summing up the first 'K' elements.
        max_score = sum(arr[:K])

        current_score = max_score
        n = len(arr)

        # Iterate from the end of the array up to 'K' elements.
        for i in range(K - 1, -1, -1):
            # Subtract the element going out of the window.
            current_score -= arr[i]

            # Add the element coming into the window from the end of the array.
            current_score += arr[n - K + i]

            # Update the maximum score if the current score is greater.
            max_score = max(max_score, current_score)

        return max_score
