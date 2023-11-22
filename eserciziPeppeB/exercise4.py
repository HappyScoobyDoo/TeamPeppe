#4. Write a function that given a list returns a string representation of it;

def stringList(list) :
    #return ' '.join(list)
    mystring = ' '
    for x in list:
        mystring += ' ' + x
    return mystring
print(stringList(["Alice","Anna","Montana"]))

