/*

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Solution 1: Using Recursion

Intuition: 

The sequence of nodes in the linked list should be that of the preorder traversal. We will take a smaller example. 

At starting node 1, what we finally want is that node 1’s right child should point to its current left child (node 2). Now If we set it like this in our preorder traversal there will be no way to reach node 3.

We need to modify our traversal technique. If we somehow start at node 3 (last node of the linked list), we need not traverse its right child as it is NULL, 
therefore we can straightaway set its right child to its left child( which is again NULL) and set its left child to NULL. 
Now we need to get to the second last node of the linked list (node 2) and set the right child to node 3. After that, we need to move to the third last node i.e node 1.

Approach: 

The algorithm steps can be stated as: 

If we observe, we are moving in a reverse postorder way : i.e  right, left, root. 
We take a reference variable (say prev) to store the previous node( initialized to NULL).
Whenever we visit a node, we set the right child to the prev and left child to NULL. 
Next we assign this current node to prev.
We perform the above two operations on all the nodes in the traversal.

  */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private TreeNode prev = null;

    public void flatten(TreeNode root) {
        if (root == null)
            return;
        flatten(root.right);
        flatten(root.left);
        root.right = prev;
        root.left = null;
        prev = root;
    }

}

/*

Time Complexity: O(N)
Reason: We are doing a simple preorder traversal.

Space Complexity: O(N)
Reason: Worst case time complexity will be O(N) (in case of skewed tree).

*/
