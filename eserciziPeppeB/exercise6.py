#Write a function that given two lists
#checks if they have common elements;

def checkList(list1,list2) :
    list=set()
    for x in list1 :
        for y in list2 :
            if(x == y) :
                list.add(x)
    return list;

print(checkList([1,2,3,"ciao"],[2,3,4,"ciao","chupa",True,1],))