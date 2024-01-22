'''

Using XOR, we are going to solve this problem using the following 3 steps.

Assume the repeating number to be X and the missing number to be Y.

Step 1: Find the XOR of the repeating number(X) and the missing number(Y)
i.e. (X^Y) = (a[0]^a[1]^…..^a[n-1]) ^ (1^2^……..^N)

In order to find the XOR of the repeating number and the missing number, we will first XOR all the array elements and with that value, we will again XOR all the numbers from 1 to N.
(X^Y) = (a[0]^a[1]^…..^a[n-1]) ^ (1^2^3^……..^N)
Step 2: Find the first different bit from right between the repeating and the missing number i.e. the first set bit from right in (X^Y)

By convention, the repeating and the missing number must be different and since they are different they must contain different bits.
Now, our task is to find the first different bit from the right i.e. the end. We know, the XOR of two different bits always results in 1. 
The position of the first different bit from the end will be the first set bit(from the right) in (X^Y) that we have found in step 1.
Step 3: Based on the position of the different bits we will group all the elements ( i.e. all array elements + all elements between 1 to N) into 2 different groups

Assume an imaginary array containing all the array elements and all the elements between 1 to N. 
Now, we will check that particular position for each element of that imaginary array and then if the bit is 0, we will insert the element into the 1st group otherwise, we will insert it into the 2nd group. 
After performing this step, we will get two groups. Now, if we XOR all the elements of those 2 groups, we will get 2 numbers. 
One of them will be the repeating number and the other will be the missing number. But until now, we do not know which one is repeating and which one is missing.

Last step: Figure out which one of the numbers is repeating and which one is missing

We will traverse the entire given array and check which one of them appears twice. And the number that appears twice is the repeating number and the other one is the missing number.

'''

def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your cod
    n = len(a)
    xr = 0

    #Step 1: Find XOR of all elements:
    for i in range(n):
        xr ^= a[i]
        xr ^= (i+1)

    #Step 2: Find the differentiating bit number:
    number = xr & ~(xr-1)
    ''' 
    bitNo = 0
    while True:
        if (xr & (1 << bitNo)) != 0:
            break
        bitNo += 1
    '''

    #Step 3: Group the numbers:
    zero, one = 0, 0
    for i in range(n):

        #part of 1 group:
        if (a[i] & number) != 0:
            one ^= a[i]
        #part of 0 group:
        else:
            zero ^= a[i]
          
    for i in range(1,n+1):
        if (i & number) != 0:
            one ^= i
        else:
            zero ^= i
        
    c = 0
    # Last step: Identify the numbers:
    for i in a:
        if i == zero:
            c += 1
    if c == 2:
        return [zero, one]
    return [one, zero]
            

'''

Time Complexity: O(N), where N = the size of the given array.
Reason: We are just using some loops running for N times. So, the time complexity will be approximately O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.

'''
