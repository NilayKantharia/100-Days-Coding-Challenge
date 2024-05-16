**LeetCode : 2331. Evaluate Boolean Binary Tree**

You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

 

Example 1:

![example1drawio1](https://github.com/NilayKantharia/100-Days-Coding-Challenge/assets/125391394/b1aaa2b7-7611-4fe7-85f1-ab299365c556)

Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
Example 2:

Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 3
Every node has either 0 or 2 children.
Leaf nodes have a value of 0 or 1.
Non-leaf nodes have a value of 2 or 3.

********

**GeeeksForGeeks : Divisibility tree**

Given a tree with n nodes where n is even. The tree is numbered from 1 to n, has n - 1 edges and is rooted at node 1. Your task is to eliminate the maximum number of edges resulting in a set of disjoint trees where the number of nodes in each tree is divisible by 2.

Example 1:

Input: 
n = 10
edges = {{2,1},{3,1},{4,3},{5,2},{6,1},{7,2},{8,6},{9,8},{10,8}}
Output:
2
Explanation:


Original tree:

![1466090203-2e0cf4f1be-even](https://github.com/NilayKantharia/100-Days-Coding-Challenge/assets/125391394/d29a4704-5fed-47b4-891a-0a88cb93b009)

   
After removing edge 1-3 and 1-6, each remaining component consists of even number of nodes. 
![image1-1](https://github.com/NilayKantharia/100-Days-Coding-Challenge/assets/125391394/29cf0743-2189-43be-b5f5-063e84581804)


Example 2:

Input: 
n = 4
edges = {{2,1},{4,2},{1,3}}
Output:
1
Explanation:
After removing 2-1, each remaining component consists of even number of nodes. 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function minimumEdgeRemove() which takes n and edges as input parameters and returns the maximum number of edges that need to be removed from the given tree.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:
1 <= n <= 105
edges.length == n - 1
1 <= edges[i][0], edges[i][1] <= n
