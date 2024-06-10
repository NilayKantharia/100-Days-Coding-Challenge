### Leetcode: 1051. Height Checker

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

 

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
 

Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100


****

### GeeksforGeeks: Nuts and Bolts Problem


Given a set of n nuts & bolts. There is a one-on-one mapping between nuts and bolts. You have to Match nuts and bolts efficiently. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means the nut can only be compared with the bolt and the bolt can only be compared with the nut to see which one is bigger/smaller.
The elements should follow the following order: { !,#,$,%,&,*,?,@,^ }

Note: Make all the required changes directly in the given arrays, output will be handled by the driver code.

Examples

Input: n = 5, nuts[] = {@, %, $, #, ^}, bolts[] = {%, @, #, $ ^}
Output: 
<code># $ % @ ^</code>
<code># $ % @ ^</code>
Explanation: As per the order # should come first after that $ then % then @ and ^. 
Input: n = 9, nuts[] = {^, &, %, @, #, *, $, ?, !}, bolts[] = {?, #, @, %, &, *, $ ,^, !}
Output: 
<code>! # $ % & * ? @ ^</code>
<code>! # $ % & * ? @ ^</code>
Explanation: We'll have to match first ! then  # , $,  %,  &,  *,  @,  ^,  ? as per the required ordering.
Expected Time Complexity: O(n(logn))
Expected Auxiliary Space: O(log(n))

Constraints:
1 <= n <= 9
The arrays 'nuts' and 'bolts' can only consist of the following elements: {'@', '#', '$', '%', '^', '&', '?', '*', '!'}.
All the elements of arrays 'nuts' and 'bolts' should be unique.
