/*

Problem statement
Stack is a data structure that follows the LIFO (Last in First out) principle. Design and implement a stack to implement the following functions:

1. Push(num): Push the given number in the stack if the stack is not full.

2. Pop: Remove and print the top element from the stack if present, else print -1.

3. Top: Print the top element of the stack if present, else print -1.

4. isEmpty: Print 1 if the stack is empty, else print 0.

5. isFull: Print 1 if the stack is full, else print 0.


You have been given ‘m’ operations which you need to perform in the stack. Your task is to implement all the functions of the stack.

*/


public class Solution{
    static class Stack {

        int[] stack;
        int top = -1;
        Stack(int capacity) {
            // Write your code here.
            this.stack = new int[capacity];
        }
        public void push(int num) {
            // Write your code here.
            if(isFull() == 0){
                this.stack[++top] = num;
            }

        }
        public int pop() {
            // Write your code here.
            if(isEmpty() == 0){
                int popElement = this.stack[top];
                top--;
                return popElement;
            }
            return -1;
        }
        public int top() {
            // Write your code here.
            if(isEmpty() == 0){
                return this.stack[top];
            }
            return -1;
        }
        public int isEmpty() {
            // Write your code here.
            if(top == -1){
                return 1;
            }
            return 0;
        }
        public int isFull() {
            // Write your code here.
            if(top == stack.length-1){
                return 1;
            }
            return 0;
        }
    }
}
