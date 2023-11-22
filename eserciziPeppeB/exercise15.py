#15. Write a function that given a integer
#in decimal returns a list of characters with the single digits as elements.

def characters(num) :
    if(isinstance(num , int)) :
        return [chr(x + 97) for x in range (num)]
print(characters(10))