""" Write a function that given
 a long string (a text) counts the words in it;"""
def countLetter(str) :
    count = 0
    for x in str :
        if not x in "_.,òà+è'ì |!£$%&/()=?^" : 
         count+=1;
    return count;

print(countLetter("vercingetorige  !!!"));