'''
Approach: 
  Use a hashmap and store as (key, value) pairs. (Can also use frequency array based on the size of nums) 
  Here the key will be the element of the array and the value will be the number of times it occurs. 
  Traverse the array and update the value of the key. Simultaneously check if the value is greater than the floor of N/2. 
    If yes, return the key 
    Else iterate forward.

'''

from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)

'''

Time Complexity: O(N*logN) + O(N), where N = size of the given array.
Reason: We are using a map data structure. Insertion in the map takes logN time. 
And we are doing it for N elements. So, it results in the first term O(N*logN). 
The second O(N) is for checking which element occurs more than floor(N/2) times.

Space Complexity: O(N) as we are using a map data structure.

'''
