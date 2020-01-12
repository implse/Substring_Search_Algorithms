# Substring Search Algorithms

In computer science, string-searching algorithms, sometimes called string-matching algorithms, are an important class of string algorithms that try to find a place where one or several strings (also called patterns) are found within a larger string or text. (wikipedia)


## Brute Force or Naïve substring search

- A simple and inefficient way to see where one string occurs inside another is to iterate through the text one by one.

- If there is a mismatch we shift the pattern one step to the right. Not efficient especially when there are a lots of matching prefixes.

ex : needle = "AAAAAB" and the haystack = "AAAAAAAAAAAAAAAB"

The average case, this takes `O(n + m)` steps, where `n` is the length of the haystack and `m`. is the length of the needle.

A substring search algorithm usually returns the index of the substring that has been found.
