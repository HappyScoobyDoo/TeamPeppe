"""10. Write a function that given a list
of strings returns the mean
length of the strings in it;"""

def listStringMean(list) :
    means = []
    for element in list :
        means.append(len(element))
    return sum(means)//len(list) 
            
print(listStringMean(["ciao","banana","suca","tre","vercingetorige"]))