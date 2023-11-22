#12. Write a function that
#given a list of numbers returns the minimum;
def minimum(list) :
    min = list[0]
    for x in list :
        if(min > x) :
            min = x
    return min
print(minimum([3,4,5,2,10,3,4,6]))