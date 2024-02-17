/*
Problem statement
You are given ‘q’ queries, where each query can be of the following types:

(1) 1 x -> this means to push the element ‘x’ in the queue.
(2) 2 -> This means deleting the front element of the queue and returning it. If there’s no element in the queue, return -1.
Your task is to implement a queue that supports these two queries.

You must write an algorithm whose time complexity is O(1), and whose space complexity is O(1).

Note:
In the output, you will see the output of queries of type 2. 
In the queries, there will be at least one type 2 query.
You will be given two functions, ‘push’, and ‘pop’. 
Your task is to implement the two functions.

Example:
Input: ‘q’ = 5
‘queries’ = [[1 3], [2], [1 4], [2], [2]]

Output: 3 4 -1

Explanation: After the first query, the queue is {3}. After the second query, the queue is {}, and we returned 3. After the third query, the queue is {4}. 
After the fourth query, the queue is {}, and we returned 4. After the fifth query, the queue is {}, and we returned -1(since there was no element at the time of the pop statement).

*/

/****************************************************************

 Following is the class structure of the Node class:

 class Node {
     public int data;
     public Node next;

     Node()
     {
         this.data = 0;
         this.next = null;
     }

     Node(int data)
     {
         this.data = data;
         this.next = null;
     }

     Node(int data, Node next)
     {
         this.data = data;
         this.next = next;
     }
 };

 class Queue{
     Node front;
     Node rear;
     void push(){};
     Queue() {
         front = null;
         rear = null;
     }
 }

 *****************************************************************/

public class Solution extends Queue{
    public void push(int x) {
        // Write Your Code Here
        Node temp = new Node(x);
        
        if(temp != null){
            if(front == null){
                front = temp;
                rear = temp;
            }
            else{
                rear.next = temp;
                rear = temp;
            }
        }
        
    }

    public int pop() {
        // Write Your Code Here
        if(front != null){
            Node prev = front;
            front = front.next;
            return prev.data;
        }
        return -1;
    }
}
