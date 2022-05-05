
s1 = list("ddhhhhhhaa")
s2 = list("aadhhhhhhd")

keyMap = {}


for index_s, s in enumerate(s1):
    print(s)
    for index_s2, char in enumerate(s2):
        if(s == char):
            if(index_s2 not in keyMap.values()): 
                keyMap[index_s2] = s 
                s2[index_s2] = '-'
                break

value = len(keyMap.keys())
if(len(keyMap.keys()) == len(s1) and len(keyMap.keys()) == len(s2)):
    print("yes")
