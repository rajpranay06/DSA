'''

Problem statement
A number is called good if it's every digit (except the rightmost digit) is larger than the sum of digits on the right side of that digit.

Find all the good numbers in the range from 'a' to 'b' (both inclusive), such that none of them contains 'digit' as a digit.

Example :
Input: 'a' = 840, 'b' = 850 and 'digit' = 6

Output: Good numbers = [840, 841, 842, 843, 850]

Explanation: Consider 841:
8 > (4 + 1)
4 > 1
Since each digit is greater than the sum of digits on right (except 1, which does not have any digit on its right), 841 is a good number. Similarly, all these numbers are good.

Sample Input 1:
20 45
1


Sample Output 1:
20 30 32 40 42 43


Explanation of sample input 1 :
The good numbers in this range are:
20 21 30 31 32 40 41 42 43

Among these, 21, 31 and 41 have digit 1 in them, so they are not included.

'''

def isGoodNumber(n, digit, s):

    if n == 0:
        return True
    
    last = n%10
    if last > s and last%10 != digit:
        s += last
        return isGoodNumber(n//10, digit, s)
    
    return False
def goodNumbers(a: int, b:int, digit:int) -> List[int]:
    
    res = []
    for i in range(a,b+1):
        if i%10 == digit:
            continue
        if isGoodNumber(i//10, digit, i%10):
            res.append(i)
    
    return res
