'''

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Time Complexity - O(N)
Space Complexity - O(N)

'''

class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        st = []

        for i in a:
            if i < 0:
                k = i
                while st and st[-1] > 0:  # If st[-1] is neg do nothing break
                    # Check if positive and neg values are colliding or not
                    k = st[-1] + i
                    # Both are same pop the stack and break
                    if k == 0:
                        st.pop()
                        break
                    # Neg val collides pos, pop the stack
                    elif k < 0:
                        st.pop()
                    # Pos collides neg, do nothing break
                    else:
                        break
                # If neg collides complete stack, push the neg
                if k < 0:
                    st.append(i)
            # Push the pos
            else:
                st.append(i)
        
        return st
