#3. Write a function that given a long string (a text)
#computes the frequencies of the vowels in it;

def vowelFrequencies(str) :
    counta = 0;
    counte = 0;
    counti = 0;
    counto = 0;
    countu = 0;
    
    for x in str :
        if x == "a" :
            counta+=1;
        if x == "e" :
            counte+=1;
        if x == "i" :
            counti+=1;
        if x == "o" :
            counto+=1;
        if x == "u" :
            countu+=1;
    return "in the word {},\t\n letter a is contained by : {},\t\n letter e is contained by : {}, \t\n letter i is contained by : {},\t\n letter o is contained by : {},\t\n letter u is contained by : {}".format(str,counta,counte,counti,counto,countu)

print(vowelFrequencies("amico"))