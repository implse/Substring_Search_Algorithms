# Knuth Morris Pratt algorithm is a substring searching algorithm

# Space : O(m)
def construct_pi_table(pattern):
    pi_table = [0]*len(pattern)
    index = 0

    for i in range(1, len(pattern)):
        if pattern[i] == pattern[index]:
            pi_table[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = pi_table[index - 1]
            else:
                pi_table[i] = 0
                i += 1
    return pi_table

# Time O(m + n)
def knuth_morris_pratt(text, pattern):
    pi_table = construct_pi_table(pattern)
    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        # matching
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            print("Pattern found at index :", str(i - j))
            j = pi_table[j - 1]
        # mismatch
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = pi_table[j - 1]
            else:
                i += 1


needle = "bebop"
haystack = "In the early 1940s, bebop-style performers began to shift jazz from danceable popular music toward a more challenging musician's music. The most influential bebop musicians included saxophonist Charlie Parker, pianists Bud Powell and Thelonious Monk, trumpeters Dizzy Gillespie and Clifford Brown, and drummer Max Roach."

print(knuth_morris_pratt(haystack, needle))
