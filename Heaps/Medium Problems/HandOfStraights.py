'''

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Approach 1 - Using Map

Intuition:
The problem asks to check if the given hand can be arranged into groupSize number of groups such that each group has consecutive numbers. 
We can solve this by using a map to count the frequency of each card in the hand and then iterating through the hand, checking if we can form consecutive groups of size groupSize.

Approach:
Create a map countMap to count the frequency of each card in the hand.
Sort the hand in ascending order.
Iterate through the hand and for each card:
a. If the frequency of the current card is 0, continue to the next card.
b. For each number in a group of size groupSize starting from the current card:
i. If the frequency of the number is 0, return false as it is not possible to form the required group.
ii. Decrement the frequency of the number in the countMap.
If we have successfully formed all groups, return true.

Complexity:
Time Complexity:
The time complexity of the solution is O(nlogn) where n is the size of the hand. This is because we sort the hand before iterating through it, which takes O(nlogn) time.
The subsequent iterations take O(n) time as we iterate through each card once.

Space Complexity:
The space complexity of the solution is O(n) as we use a map to store the frequency of each card in the hand. In the worst case, if all cards in the hand are unique, the map will have n entries.

'''

class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:

        n = len(hand)
        if n%k != 0:
            return False

        count = {}
        for key in hand:
            count[key] = count.get(key, 0) + 1
        
        hand.sort()
        for key in hand:
            if count[key] == 0:
                continue
            
            for j in range(k):
                currChar = key + j
                if count.get(currChar, 0) == 0:
                    return False
                count[currChar] -= 1
        
        return True


'''

Approach - Without using map

'''

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize >0:
            return False
        
        total_count = len(hand)//groupSize
        count = 0
        hand.sort()

        while len(hand) > 0:
            
            # Pop the last element
            h = hand.pop()
            # We are decrementing -1 from size as we selected one card
            size = groupSize - 1
            # the popped index
            popi = len(hand)-1
            while popi > -1 and size > 0:
                # If popped index card is same as popped crad move beck one index
                if hand[popi] == h:
                    popi -= 1
                # If card-1 is not present return false 
                elif hand[popi] != h -1:
                    return False
                else:
                    # If card-1 is present, pop it move back index, decrease size 
                    h = hand.pop(popi)                       
                    popi -=1
                    size -=1
            count += 1
        
        return count == total_count

'''

Time Complexity - O(N*K)
Space Complexity - O(1)

'''
