'''

Given an integer n, return the number of prime numbers that are strictly less than n.

Intuition of Sieve of Eratosthenes is we will mark all the multiples of a number from thw number to n. 

If 10 is given, we will start from 2 and mark 4, 6, 8, 10 as not primes. Next 3 mark 6, 9. 4 is already marked. Take 5 mark 10. 6 is marked. 7 there is no 14. 8 9 10 are marked.
O/p would be 2, 3, 5, 7.

We don't need to traverse whole 2 to n, we can traverse from 2 to sqrt of n. 

Time Complexity - O(Nlog(log(N))), where ‘N’ is the given number.
We are using the Sieve of Eratosthenes, so our complexity is O(Nlog(log(N))).

Space Complexity - O(N), where ‘N’ is the given number.

'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: 
            return 0
        a = [1] * n
        a[0] = a[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if a[i]==0:
                continue
            # Marking all the multiples of i 
            a[i*i: n: i] = [0] * (len(a[i*i: n: i]))
        return sum(a)
