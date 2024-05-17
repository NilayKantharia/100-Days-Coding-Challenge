**LeetCode : 1325. Delete Leaves With a Given Value**

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

Example 1:

![sample_1_1684](https://github.com/NilayKantharia/100-Days-Coding-Challenge/assets/125391394/bc9bd277-867b-402d-92cf-39b227f47982)



Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).


Example 2:

![sample_2_1684](https://github.com/NilayKantharia/100-Days-Coding-Challenge/assets/125391394/f6356da9-e351-43c5-beb8-20a011aaaf6a)


Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]


Example 3:

![sample_3_1684](https://github.com/NilayKantharia/100-Days-Coding-Challenge/assets/125391394/a16696aa-edb4-4793-ba6f-527fc70fd0da)


Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000


********

**GeeksForGeeks : Find Pair Given Difference**

Given an array arr[] of size n and an integer x, return 1 if there exists a pair of elements in the array whose absolute difference is x, otherwise, return -1.

Example 1:

Input:
n = 6
x = 78
arr[] = {5, 20, 3, 2, 5, 80}
Output:
1
Explanation:
Pair (2, 80) have absolute difference of 78.
Example 2:

Input:
n = 5
x = 45
arr[] = {90, 70, 20, 80, 50}
Output:
-1
Explanation:
There is no pair with absolute difference of 45.
Your Task:
You need not take input or print anything. Your task is to complete the function findPair() which takes integers n, x, and an array arr[] as input parameters and returns 1 if the required pair exists, return -1 otherwise.

Expected Time Complexity: O(n* Log(n)).
Expected Auxiliary Space: O(1).

Constraints:
1<=n<=106 
1<=arr[i]<=106 
0<=x<=105

