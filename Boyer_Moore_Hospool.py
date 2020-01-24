# Boyer Moore Hospool algorithm is a substring searching algorithm

# Time O(n)
def preprocess(needle):
    bad_match_table = dict()
    for index, char in enumerate(needle):
        max_shift = max(1, len(needle) - index - 1)
        bad_match_table[char] = max_shift
    return bad_match_table

def boyer_moore(needle, haystack):
    table = preprocess(needle)
    index = 0
    while len(haystack) - len(needle) >= index:
        offset = 0
        for j in reversed(range(len(needle) - 1)):
            if haystack[index+j] != needle[j]:
                offset = table.get(haystack[index + j], len(needle))
                index += offset
                break
        if offset == 0:
            return index
    return -1

needle = "jazz"
haystack = "New Orleans jazz begin in 1910"

s = "ATErUUeUkVFVNfxfUKtntOErKmZLUpWpHRASdxjUhzzxygmnNnKabPPgPqy vCLSCZObaNNGCXQssfEEDDJIPBwtkMmTniKa pBlrd"
x =  "vCLSCZObaNNGCXQssfEEDDJIPBwtkMmTniKa"
# ATErUUeUkVFVNfxfUKtntOErKmZLUpWpHRASdxjUhzzxygmnNnKabPPgPqy vCLSCZObaNNGCXQssfEEDDJIPBwtkMmTniKa pBlrd
print(boyer_moore(needle, haystack))
print(boyer_moore(s, x))

# Time O(n+m)
def boyer_moore(needle, haystack):
    table = preprocess(needle)
    offset = 0

    while len(haystack) - offset >= len(needle):
        i = len(needle) - 1
        while haystack[offset + i] == needle[i]:
            if i == 0:
                return offset
            i -= 1
        offset += table.get(haystack[offset + len(needle) - 1], len(needle))
    return -1

def preprocess(word):
    table = dict()
    for i in range(len(word) - 1):
        table[word[i]] = len(word) - i - 1
    return table

needle = "peintre" # 7
haystack = "Théodore Géricault est un peintre, sculpteur, dessinateur et lithographe français." # 82

print(boyer_moore(needle, haystack))
