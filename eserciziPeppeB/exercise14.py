#14. Write a function that given a list of numbers returns the quartiles;
def quartiles(list) :
    sorted(list)
    return [x for x in list if (x == list[len(list)//4])]

print(quartiles([1,3,5,7,8,10]))