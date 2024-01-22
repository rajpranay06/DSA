'''

You are given a read-only array of N integers with values also in the range [1, N] both inclusive. 
Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

Input Format:  array[] = {3,1,2,5,3}
Result: {3,4)
Explanation: A = 3 , B = 4 
Since 3 is appearing twice and 4 is missing

Approach:

Step 1: Form equation 1:

Now, we know the summation of the first N numbers is: Sn = (N*(N+1))/2

Let’s say, S = the summation of all the elements in the given array.

Therefore, S - Sn = X - Y…………………equation 1

Step 2: Form equation 2:

Now, we know the summation of squares of the first N numbers is:

S2n = (N*(N+1)*(2N+1))/6
Let’s say, S2 = the summation of squares of all the elements in the given array.

Therefore, S2-S2n = X2-Y2...................equation 2
From equation 2 we can conclude,

X+Y = (S2 - S2n) / (X-Y) [From equation 1, we get the value X-Y] ………… equation 3
From equation 1 and equation 3, we can easily find the value of X and Y. And this is what we want.

'''

def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your cod
    n = len(a)

    # Find Sn and S2n:
    numbersSum = n*(n+1)//2
    squareSum = n*(n+1)*((2*n)+1)//6

    # Calculate S and S2:
    arrSum = 0
    arrSquareSum = 0
    for i in a:
        arrSum += i
        arrSquareSum += (i*i)

    # S-Sn = X-Y:
    val1 = arrSum - numbersSum
    
    # S2-S2n = X^2-Y^2:
    val2 = arrSquareSum - squareSum

    # Find X+Y = (X^2-Y^2)/(X-Y):
    val2 = val2//val1

    # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
    # Here, X-Y = val1 and X+Y = val2:
    x = (val1+val2)//2
    y = x - val1

    return [x,y]
    

'''

Time Complexity: O(N), where N = the size of the given array.
Reason: We are using only one loop running for N times. So, the time complexity will be O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem

'''

