'''

Problem statement
The Road Department is planning to make some new traffic regulations. But to make the regulations they need to analyze the current situation of the traffic.
The traffic can be analyzed from an array 'VEHICLE' of length 'N' , which consists of ‘0’ if there is no vehicle at that point and ‘1’ if there is a vehicle at the point.
Unfortunately the array ‘VEHICLE’ got corrupted as at most 'M' '1' got flipped to ‘0’.
Traffic jam is defined as the length of consecutive vehicles on the road.
The Road Department wants to know the worst possible scenario for the traffic jam. Return the maximum possible length of the consecutive vehicles.

Example:
Input: ‘N’ = 3, ‘M’ = 1, VEHICLE’ = [0, 1, 1]
Output: 3

Explanation:
As there is at most one 1 that got flipped to 0, so for the worst-case scenario we can reflip the first(1-based ) index to 1, resulting in a length of 3. 

'''

def traffic(n: int, m: int, a: [int]) -> int:
    # Write your code here.
    
    c = 0
    maxL = 0
    j = 0

    for i in range(n):

        # Incrementing the count
        if a[i] == 0:
            c += 1
        
        # Removing indices till count == k
        while c > m: 
            if a[j] == 0:
                c -= 1
            j += 1
        
        maxL = max(maxL, i-j+1)

    return maxL

'''

Time Complexity - O(N)

Space Complexity - O(1)

'''
