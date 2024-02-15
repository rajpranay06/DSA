'''

Problem statement
Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.

For example:
'N' = 5.
The divisors of 5 are 1, 5.

According to Number theory, any number has at least 2 divisors (1, the number itself), and if the number ‘A’ is a divisor of the number ‘B’, then the number ‘B’ / ‘A’ is also a divisor of the number ‘B’. 
Now consider a pair of numbers ‘X’, and ‘Y’, such that ‘X’ * ‘Y’ == 'B'. If 'X' == 'Y' == sqrt(B), then it is obvious that ‘X’, ‘Y’ <= sqrt(B). 
If we try to increase 'Y', then we have to reduce ‘X’ so that their product is still equal to 'B'. 
So it turns out that among any pair of numbers ‘X’, and ‘Y’, which in the product give ‘B’, at least one of the numbers will be <= sqrt(B). 
Therefore it is enough to find simply all divisors of number ‘B’ which <= sqrt(B).
Iterate through all the numbers from 1 to sqrt('N'), and check if that number (let's say ‘x’) divides ‘N’, and if it divides, add that to our answer array.
If ‘x’ divides ‘N’, then ‘N’/'x' will also divide ‘N’, so add that also to our answer array.


Time Complexity - O(sqrt(N)), where ‘N’ is the given number.
We are traversing from 1 to sqrt(N), So the space complexity is O(sqrt(N)).

Space Complexity - O(1).
We use constant extra space, So the space complexity is O(1).

'''


def printDivisors(n: int) -> List[int]:
    ans = []

    # Traversing from 1 to sqrt(N).
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans.append(i)
            if n // i != i:
                ans.append(n // i)

    ans.sort()
    return ans
