def canConstruct(ransomNote = "aab", magazine = "a"):
    constructed = ''
    for i in ransomNote:
        if magazine and i in magazine:
            constructed += i
            magazine = magazine.replace(i, '', 1)

    return constructed == ransomNote


print(canConstruct())
