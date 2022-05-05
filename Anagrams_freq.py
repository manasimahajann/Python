import re
from unittest.main import main


s1= "gardreenrrre"
s2 = "dangwrerrrer"

freq_s1 = {}
freq_s2 = {}

def are_anagrams():
    if len(s1)!= len(s2):
        return False

    for s in s1:
        if s in freq_s1.keys():
            freq_s1[s] += 1
        else:
            freq_s1[s] = 1

    for s in s2:
        if s in freq_s2.keys():
            freq_s2[s] += 1
        else:
            freq_s2[s] = 1

    for key in freq_s1:
        if key not in freq_s2 or freq_s1[key] != freq_s2[key]:
            return False 

    return True
    # if(freq_s2 == freq_s1):
    #     return True
    # else:
    #     return False

if __name__ == '__main__':

    print(are_anagrams())