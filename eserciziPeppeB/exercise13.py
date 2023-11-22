#13. Write a function that given a list of
#numbers returns the median;

def median(list) :
    sorted(list)
    a = (len(list) % 2 == 0) if [x for x in list if(x == list[len(list)//2-1])] else [x for x in list if(x == list[len(list)//2])]
    b = (len(list) % 2 == 0) if [x for x in list if(x == list[len(list)//2])] else [x for x in list if(x == list[len(list)//2+1])]
    return sum(a+b)/2
print(median([2,3,4,5]))
print(median([1,4,6,7,10,14,32]))        

