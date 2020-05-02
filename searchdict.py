def searchDict(dictionary, word): 
    if word == '': 
        return True
    else: 
        n = len(word) 
        return any([(word[:i] in dictionary) and searchDict(dictionary, word[i:]) for i in range(1, n+1)]) 


print(searchDict({"i", "like", "sung", "samsung"}, "ilike"))