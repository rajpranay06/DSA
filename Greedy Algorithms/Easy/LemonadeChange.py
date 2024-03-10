'''

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Example 1:

Input: bills = [5,5,5,10,20]
Output: true

Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0] * 2

        for bill in bills:
            if bill == 5:
                changes[0] += 1
            elif bill == 10:
                changes[0] -= 1
                changes[1] += 1
            else:
                if changes[1] > 0:
                    changes[1] -= 1
                    changes[0] -= 1
                else:
                    changes[0] -= 3
            if changes[0] < 0:
                return False

        return True
        
