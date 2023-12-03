#1. Write a function that counts the NOT vowels in a string;
def countNotVowels(string) :
    count = 0;
    for c in string :
        if not c in "aeiou":
            count+=1
    return count

print(countNotVowels("Pdirc"))
print("ciao mamma sono in tv")
print("Ti voglio bene mamma")
print("Sono la tua vita")
print("ti prego sii felice")
print("provo ad applicare lo stash")
print("test1")
