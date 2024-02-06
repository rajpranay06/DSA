'''

Problem statement
You are given a stack ‘S’. Your task is to sort the sack recursively.

Note:
Looping through the stack is not allowed.
You need to return a stack that is sorted in descending order.

For example:
Given stack S = 1 3 2 
The output will be 3 2 1 since it is the sorted order.


Sample Input 1 :
2
4
1 0 0 2 
3 
2 4 2
Sample Output 1 :
2 1 0 0
4 4 2

'''

def sortStackRecursive(s, element):

    if not s or s[-1] < element:
        s.append(element)
        return
    
    top_element = s.pop()
    
    sortStackRecursive(s, element)

    s.append(top_element)

def sortStack(s):
    # Write your code here.
    if not s:
        return s
    
    element = s.pop()
    
    sortStack(s)

    sortStackRecursive(s, element)

    return s
