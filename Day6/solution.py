def groupAnagrams(strs):
    anagram_dict = {}
    for x in strs:
        l = list(x)
        l.sort()
        temp = "".join(l)
        if anagram_dict.get(temp):
            anagram_dict[temp].append(x)
        else:
            anagram_dict[temp] = [x]
    return list(anagram_dict.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))