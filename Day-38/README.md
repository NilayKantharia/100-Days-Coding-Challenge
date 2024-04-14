**LeetCode : 404. Sum of Left Leaves**
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

************

************

**GeeksForGeeks : Xoring and Clearing**

You are given an array arr[] of size n. You need to do the following:

You need to calculate the bitwise XOR of each element in the array with its corresponding index (indices start from 0).
After step1, print the array.
Now, set all the elements of arr[] to zero.
Now, print arr[].
Example 1:

Input:
n = 10
arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Output:
1 3 1 7 1 3 1 15 1 3
0 0 0 0 0 0 0 0 0 0
Explanation:
First we take xor of every element with
their indices, like (1xor0), (2xor1), (3xor2), (4xor3) and so on.
Now print the resultant array
Now set all the elements of array to zero
Now print the resultant array
Example 2:

Input:
n = 4
arr[] = {10, 20, 30, 40}
Output:
10 21 28 43
0 0 0 0
Explanation:
First we take xor of every element with
their indices, like (1xor0), (2xor1), (3xor2).
Now print the resultant array
Now set all the elements of array to zero
Now print the resultant array
Your Task:
Since this is a function problem, you don't need to take any input. Just complete the provided functions. In a new line, print the output.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 1000
1 <= arr[i] <= 1000
