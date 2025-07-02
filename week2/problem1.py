def isSameReflection(word1, word2):
    if len(word1) != len(word2):
        return -1
    
    doubled = word1 + word1
    if word2 in doubled:
        return 1
    else:
        return -1

print(isSameReflection("sample", "plesam")) 
print(isSameReflection("sample", "examples"))  