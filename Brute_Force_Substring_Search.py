# Naive

def naive_search(needle, haystack):
    offset = 0
    while len(haystack) - offset >= len(needle):
        i = 0
        while haystack[i + offset] == needle[i]:
            if i == len(needle) - 1:
                return offset
            i += 1
        offset += 1
    return -1

needle = "jazz" # 7
haystack = "Ornette Coleman, né le 9 mars 1930 à Fort Worth (Texas) est un saxophoniste ténor et alto, trompettiste, violoniste et compositeur, précurseur majeur du free jazz."
