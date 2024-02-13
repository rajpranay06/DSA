/*

Problem statement
For a given integer 'N', you have to return the number of set bits in the binary representation of the numbers from 1 to 'N'.
In a binary number '1' is considered as a set bit and '0' as not set.

Example:
If 'N' is 4, then

1 has a binary representation of 1
2 has a binary representation of 10
3 has a binary representation of 11
4 has a binary representation of 100

Hence number of set bits is 5.

*/

public class Solution{
    public static int largestPowOf2(int n){
        int x=0;
        while((1<<x)<=n){
            x++;
        }
        return x-1;
    }
    public static int countSetBits(int n) {
        if(n==0){
            return 0;
        }
        int p=largestPowOf2(n);
        return p*(1<<(p-1)) + n-(1<<p)+1 + countSetBits(n-(1<<p));
    }
}
