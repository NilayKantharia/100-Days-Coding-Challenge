### Leetcode: 648. Replace Words

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.

### GeeksforGeeks: Maximum occured integer

Given n integer ranges, the task is to return the maximum occurring integer in the given ranges. If more than one such integer exists, return the smallest one.
The ranges are in two arrays l[] and r[].  l[i] consists of the starting point of the range and r[i] consists of the corresponding endpoint of the range & a maxx which is the maximum value of r[].

For example, consider the following ranges.
l[] = {2, 1, 3}, r[] = {5, 3, 9)
Ranges represented by the above arrays are.
[2, 5] = {2, 3, 4, 5}
[1, 3] = {1, 2, 3}
[3, 9] = {3, 4, 5, 6, 7, 8, 9}
The maximum occurred integer in these ranges is 3.

Examples :

Input: n = 4, l[] = {1,4,3,1}, r[] = {15,8,5,4}, maxx = 15
Output: 4
Explanation: The given ranges are [1,15] [4, 8] [3, 5] [1, 4]. The smallest number that is most common or appears most times in the ranges is 4.
Input: n = 5, l[] = {1,5,9,13,21}, r[] = {15,8,12,20,30}, maxx = 30
Output: 5
Explanation: The given ranges are [1, 15] [5, 8] [9, 12] [13, 20] [21, 30]. The smallest number that is most common or appears most times in the ranges is 5.
Expected Time Complexity: O(n+maxx).
Expected Auxiliary Space: O(maxx), maxx is maximum element in r[]

Constraints:
1 ≤ n ≤ 106
0 ≤ l[i], r[i] ≤ 106
