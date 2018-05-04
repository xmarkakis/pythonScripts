# -*- coding: utf-8 -*-
"""
Created by xmarkakis on May 3rd, 2018.
This is a script to convert numbers into roman numeral. It really only supports numbers under 1000 and years (up to 5000).
Reason being, roman numerals have weird characters for 5,000 and above. Since I hanve't found a way to insert those special characters,
I just added the lower case values of those characters in the mean time.
"""
romanNum = {"a":"I","b":"V","c":"X","d":"L","e":"C","f":"D","g":"M","h":"v","i":"x"}
            
def checkLen(x):
    #keep in mind that negative values will fall into the wrong length category!!

#The first if statement handles 4 integer length number inserts. 
    if len(x)==4:
        print("length is 4")
        m = list(x)
        print(m)
        return romanIV(m[0]) + romanIII(m[1]) + romanII(m[2]) + romanI(m[3])

#The second if statement handles 3 integer length number inserts.    
    elif len(x)==3:
        print("length is 3")
        m = list(x)
        print(m)
        return romanIII(m[0]) + romanII(m[1]) + romanI(m[2])

#The third if statement handles 2 integer length number inserts.    
    elif len(x)==2:
        print("length is 2")
        m = list(x)
        print(m)
        return romanII(m[0]) + romanI(m[1])

#The last if statement handles 1 integer length number inserts.         
    elif len(x)==1:
        print("length is 1")
        m = list(x)
        if m == 0: 
            return ""
        else:
            return romanI(x)

#Just some fun return statement for users that enter more than 4 characters        
    elif len(x)>4:
        print("Nice Try ;-)")
    
    else:
        print("Please print a value in range")

def romanI(x):
    a=int(x)
    if a==0 or a==5:
        if a==5:
            p = romanNum["b"]
            return p
        else:
            return ""
    elif a==4 or a==9:
        if a==4:
            x=romanNum["a"]
            y=romanNum["b"]
            p=x+y
            return p
        else:
            x=romanNum["a"]
            y=romanNum["c"]
            p=x+y
            return p
    elif a>0 and a<9:
        if a<4:
            p=a*romanNum["a"]
            return p
        else:
            x=(a-5)*romanNum["a"]
            y=romanNum["b"]
            p=y+x
            return p
    else:
        return "z1"
        
def romanII(x):
    a=int(x)
    if a==0 or a==5:
        if a==5:
            p = romanNum["d"]
            return p
        else:
            return ""
    elif a==4 or a==9:
        if a==4:
            x=romanNum["c"]
            y=romanNum["d"]
            p=x+y
            return p
        else:
            x=romanNum["c"]
            y=romanNum["e"]
            p=x+y
            return p
    elif a>0 and a<9:
        if a<4:
            p=a*romanNum["c"]
            return p
        else:
            x=(a-5)*romanNum["c"]
            y=romanNum["d"]
            p=y+x
            return p
    else:
        return "z1"
        
def romanIII(x):
    a=int(x)
    if a==0 or a==5:
        if a==5:
            p = romanNum["f"]
            return p
        else:
            return ""
    elif a==4 or a==9:
        if a==4:
            x=romanNum["e"]
            y=romanNum["f"]
            p=x+y
            return p
        else:
            x=romanNum["e"]
            y=romanNum["g"]
            p=x+y
            return p
    elif a>0 and a<9:
        if a<4:
            p=a*romanNum["e"]
            return p
        else:
            x=(a-5)*romanNum["e"]
            y=romanNum["g"]
            p=y+x
            return p
    else:
        return "z1"

def romanIV(x):
    a=int(x)
    if a==0 or a==5:
        if a==5:
            p = romanNum["h"]
            return p
        else:
            return ""
    elif a==4 or a==9:
        if a==4:
            x=romanNum["g"]
            y=romanNum["h"]
            p=x+y
            return p
        else:
            x=romanNum["g"]
            y=romanNum["i"]
            p=x+y
            return p
    elif a>0 and a<9:
        if a<4:
            p=a*romanNum["g"]
            return p
        else:
            x=(a-5)*romanNum["g"]
            y=romanNum["i"]
            p=y+x
            return p
    else:
        return "z1"

        #case 2 - When the value is zero, need to return the function somehow to the next function
#remember to convert values to int and abs so that you change the string into a value and also get the absolute value as well
numX = input("Enter a number to turn into a number: ")
print(checkLen(numX))


