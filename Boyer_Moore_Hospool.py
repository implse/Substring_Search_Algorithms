# Boyer Moore Hospool algorithm is a substring searching algorithm

def boyer_moore(needle, haystack):
    table = preprocess(needle)
    offset = 0
    i = len(needle) - 1
    while len(haystack) - offset >= len(needle):
        if same(haystack[offset + i], needle):
            return offset
        i -= 1
    return -1

def same(str1, needle):
    i = len(needle) - 1
    while str1[i] == needle[i]:
        if i == 0:
            return True
        i -= 1
    return False

def preprocess(word):
    table = dict()
    for i in range(len(word) - 1):
        table[word[i]] = len(word) - i - 1
    return table

needle = "peintre" # 7
haystack = "Théodore Géricault est un peintre, sculpteur, dessinateur et lithographe français." # 82

print(boyer_moore(needle, haystack))
