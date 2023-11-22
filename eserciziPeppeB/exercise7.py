#Write a function that capitalizes 
#all (and only) the vowels in a string;

def vowelCapitalize(str) :
    res=""
    for x in str :
        if x in "aeiou" :
            res+= x.upper()
        else :
            res+= x
    return res

print(vowelCapitalize("ciaoputtana"))