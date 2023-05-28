# 242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

## Solution 1

- sort both string then compare if they are same
_for example_:`anagram` after sorted `aaagrm` and `nagaram` after sort `aaagrm`
so we can say `true` same for `rat`=>`art`, `car`=>`acr` so `false`

## Solution 2

- use python Counter() to compare if same `true` else `false`
_Example_: return Counter(s) == Counter(t)