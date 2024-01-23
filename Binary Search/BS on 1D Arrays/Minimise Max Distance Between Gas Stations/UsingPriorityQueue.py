'''

You are given a sorted array ‘arr’ of length ‘n’, which contains positive integer positions of ‘n’ gas stations on the X-axis. You are also given an integer ‘k’. 
You have to place ‘k’ new gas stations on the X-axis. You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions. 
Let ‘dist’ be the maximum value of the distance between adjacent gas stations after adding k new gas stations.
Find the minimum value of ‘dist’.

Note: Answers within 10^-6 of the actual answer will be accepted. For example, if the actual answer is 0.65421678124, it is okay to return 0.654216. 
Our answer will be accepted if that is the same as the actual answer up to the 6th decimal place.

Input Format: n1 = 3, arr1[] = {2,4,6}, n2 = 3, arr2[] = {1,3,5}
Result: 3.5
Explanation: The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 5, 6 }. As the length of the merged list is even, the median is the average of the two middle elements. 
Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.

In each iteration, we will identify the index ‘i’ where the distance (arr[i+1] – arr[i]) is the maximum. Then, we will insert new stations into that section to reduce that maximum distance. 
The number of stations inserted in each section will be tracked using the previously declared array of size n-1.

Finally, after placing all the stations we will find the maximum distance between two consecutive stations. 
To calculate the distance using the previously discussed formula, we will just do as follows for each section:
distance = section_length / (number_of_stations_ inserted+1)

Instead of using a loop to find the maximum distance, we can simply use the heap data structure i.e. the priority queue.

Thus using a priority queue, we can optimize the search for the maximum distance. 
We will use the max heap implementation and the elements will be in the form of pairs i.e. <distance, index> as we want the indices sorted based on the distance. 
As we are using max heap the maximum distance will always be the first element.

'''

import heapq

def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of array.
    howMany = [0] * (n - 1)
    pq = []

    # insert the first n-1 elements into pq
    # with respective distance values:
    for i in range(n - 1):
        heapq.heappush(pq, ((-1)*(arr[i + 1] - arr[i]), i))

    # Pick and place k gas stations:
    for gasStations in range(1, k + 1):
        # Find the maximum section
        # and insert the gas station:
        tp = heapq.heappop(pq)
        secInd = tp[1]

        # insert the current gas station:
        howMany[secInd] += 1

        inidiff = arr[secInd + 1] - arr[secInd]
        newSecLen = inidiff / (howMany[secInd] + 1)
        heapq.heappush(pq, (newSecLen*(-1), secInd))

    return pq[0][0]*(-1)

'''

Time Complexity: O(nlogn + klogn),  n = size of the given array, k = no. of gas stations to be placed.
Reason: Insert operation of priority queue takes logn time complexity. O(nlogn) for inserting all the indices with distance values and O(klogn) for placing the gas stations.

Space Complexity: O(n-1)+O(n-1)
Reason: The first O(n-1) is for the array to keep track of placed gas stations and the second one is for the priority queue.

'''
