#5. Write a function that given a list
# of numbers gives back the product of all its elements;

def multiplyList(list) :
    res = 1
    for i in list :
        if (isinstance(i, int)) :
            res *= i
    return res    

print(multiplyList(["3","3",True,2,"ciao",4]))