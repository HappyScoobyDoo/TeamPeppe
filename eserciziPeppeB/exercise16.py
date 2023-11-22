#16. Write a function that given a string in roman literals returns the decimal value (use only 
#“additive roman numerals”.

def romanToDecimal(sentence) :
    res = 0   
    if(isinstance(sentence, str)) :
        for x in sentence :
            if(x == "i".lower()) :
                res+=1
            elif(x == "v".lower()) :
                res+=5
            elif(x == "x".lower()) :
                res+=10
            elif(x == "l".lower()) :
                res+=50
            elif(x == "c".lower()) :
                res+=100
            elif(x == "d".lower()) :
                res+=500
            elif(x == "m".lower()) :
                res+=1000
        return res
    
print(romanToDecimal("xiii"))