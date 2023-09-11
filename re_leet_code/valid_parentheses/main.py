from collections import Counter

def isValid(s: str) -> bool:
    # parentheses = list(s)
    # for i in range(len(parentheses)):
    parentheses_dict = Counter(s)
    if parentheses_dict["("] != parentheses_dict[")"]:
        return False
    elif parentheses_dict["{"] != parentheses_dict["}"]:
        return False
    elif parentheses_dict["["] != parentheses_dict["]"]:
        return False
    return True


s = "()[]{}"
print(isValid(s))
