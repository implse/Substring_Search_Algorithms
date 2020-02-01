# Substring Search Algorithms

In computer science, string-searching algorithms, sometimes called string-matching algorithms, are an important class of string algorithms that try to find a place where one or several strings (also called patterns) are found within a larger string or text. (wikipedia)

The string match problem also known as "the needle in a haystack" has a lot of application :

  - Pattern recognition
  - Document matching
  - DNA matching


## Brute Force or Naïve substring search

- A simple and inefficient way to see where one string occurs inside another is to iterate through the text one by one.

- If there is a mismatch we shift the pattern one step to the right. Not efficient especially when there are a lots of matching prefixes.

ex : needle = "AAAAAB" and the haystack = "AAAAAAAAAAAAAAAB"

The average case, this takes `O(n*m)` steps, where `n` is the length of the haystack and `m`. is the length of the needle.

A substring search algorithm usually returns the index of the substring that has been found.

## Boyer Moore

- Boyer–Moore string search algorithm is an efficient string searching algorithm that is the standard benchmark for practical string-search literature.

- The algorithm pre-process the string being searched for (the pattern or needle), but not the string being searched in (the text or haystack).

- The algorithm runs faster as the length of the pattern increase.

#### Mad Match Table

This table defines how many letters to shift the pattern when a mismatch occurs.

This table never has elements smaller than 1.

bad match table formula : `max(1, len(needle) - index - 1)`

We keep comparing the pattern to the text starting from the rightmost character in the pattern. When mismatch occurs we have to shift the pattern to the right corresponding to the value in the bad match table.

Because unlike brute force search we can skip several characters in one iteration the algorithm will be faster.

The average time complexity is `O(m+n)` steps, where `n` is the length of the haystack and `m` is the length of the needle.

The worst case time complexity is `O(n*m)`.

## Knuth Morris Pratt

The KMP is a linear time algorithm that exploits the observation that every time a match or a mismatch happens,
the pattern itself contains enough information to dictate where the new examination should begin from.

- The algorithm must preprocess the pattern with `O(m)` additional space complexity.
- Knuth Morris Pratt has `O(n + m)` linear running time complexity even in the worst-case scenario.
