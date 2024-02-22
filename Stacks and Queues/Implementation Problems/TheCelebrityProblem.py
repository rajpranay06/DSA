'''

Problem statement
There are ‘N’ people at a party. Each person has been assigned a unique id between 0 to 'N' - 1(both inclusive). A celebrity is a person who is known to everyone but does not know anyone at the party.

Given a helper function ‘knows(A, B)’, It will returns "true" if the person having id ‘A’ know the person having id ‘B’ in the party, "false" otherwise. 
Your task is to find out the celebrity at the party. Print the id of the celebrity, if there is no celebrity at the party then print -1.

Note:
1. The helper function ‘knows’ is already implemented for you.
2. ‘knows(A, B)’ returns "false", if A doesn't know B.
3. You should not implement helper function ‘knows’, or speculate about its implementation.
4. You should minimize the number of calls to function ‘knows(A, B)’.
5. There are at least 2 people at the party.
6. At most one celebrity will exist.

'''

from os import *
from sys import *
from collections import *
from math import *

'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):

    st = [] 
    # Push all the ids into stack
    for i in range(n):
        st.append(i)
    # Pop the first two ids and check which id knows which
    while len(st) > 1:
        a = st.pop()
        b = st.pop()
        if knows(a,b):
            st.append(b)
        else:
            st.append(a)
    # If no one is celebrity
    if not st:
        return -1
    
    potentialCeleb = st.pop()
    # Check if all ids knows potemntialCeleb, except itself
    for i in range(n):
        if i != potentialCeleb:
            if not knows(i, potentialCeleb):
                return -1
    
    # Check if potentialCeleb doesn't know other ids, except itself
    for i in range(n):
        if i != potentialCeleb:
            if knows(potentialCeleb, i):
                return -1
    
    return potentialCeleb


