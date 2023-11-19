#11. Write a function that
#given a list of numbers returns the maximum;
def maximum(list) :
    max = list[0]
    for x in list :
        if(max < x) :
            max = x
    return max
print(maximum([3,4,5,10,3,4,6]))