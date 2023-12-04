#1. Write a function that counts the NOT vowels in a string;
def countNotVowels(string) :
    count = 0;
    for c in string :
        if not c in "aeiou":
            count+=1
    return count

print(countNotVowels("Pdirc"))
print("Faustino")
print("Test che collide su b2")
