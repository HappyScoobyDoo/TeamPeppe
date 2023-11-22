"""Write a function that given a list
returns a list with three lists as elements:
one for the numbers, one for
the strings and one for the boolean;"""

def threeList(list) :
    return [
           [x for x in list if (isinstance(x, int) and not isinstance(x, bool))],
           [x for x in list if isinstance(x, str)],
           [x for x in list if isinstance(x, bool)]
    ]


print(threeList(["ciao","suca","merda",2,1,3,True,False]))