# -*- coding: utf-8 -*-
"""
Created by xmarkakis on May 3rd, 2018.
This is a script to convert numbers into roman numeral. It really only supports numbers under 1000 and years (up to 5000).
Reason being, roman numerals have weird characters for 5,000 and above. Since I hanve't found a way to insert those special characters,
I just added the lower case values of those characters in the mean time.
"""
romanNum = {"a":"I","b":"V","c":"X","d":"L","e":"C","f":"D","g":"M","h":"v","i":"x"}
"""
This is a temp version of the final script. I've overhauling all the code from the original. 
I'm determined to get this script down to a simple few lines. Here are the steps I think the script needs to do:
1. Check if the length of the user input is less than 5 (anything greater than 4 should generate an error)
2. Check if the first character in the string is a negative sign. 
3. Check if the value can be converted into a string. (Look into how this can be done. I'm thinkng a simple if statement that returns true.)
4. Create a function that grans the values and it's index position to evaluate the number independent of the other numbers. 
5. Add the outputs together to generate an accurate roman numeral (need to make sure the "for" loop here evaluates the numbers and adds them in order.)   
"""
numX = input("Enter a number to turn into a numeral: ")
#def checkLen2(x):
    #m = list(x)
    #print(m)
    #print(m[:1])
    #if x[0:1]=='-':
      #  m=list(x)
     #    print(m)
   #     print("Yes")
  #  else:
 #       print("No")
#print(checkLen2("-150"))

def negCheck(x):
    if x[:1]=='-':
        m=list(x)
        return checkLen(m[1:])
    else:
        m=list(x)
        return checkLen(m)

def checkLen(x):
#keep in mind that negative values will fall into the wrong length category!!
#4 integer length check. 
    if len(x)==4:
        return romanIV(x[0]) + romanIII(x[1]) + romanII(x[2]) + romanI(x[3])
        print(x)

#3 integer length check.    
    elif len(x)==3:
        print(x)
        return romanIII(x[0]) + romanII(x[1]) + romanI(x[2])

#2 integer length check.   
    elif len(x)==2:
        print(x)
        return romanII(x[0]) + romanI(x[1])

#Single integer length check.         
    elif len(x)==1:
        if x == 0: 
            print("You entered 0 .... 0 is 0 in roman numerals .... come on!!")
        else:
            return romanI(x)

#Just some fun return statement for users that enter more than 4 characters        
    elif len(x)>4:
        print("Nice Try ;-)")
    
    else:
        print("Please print a value in range")

def romanI(x):
    a=abs(int(x))
    #evaluates when the number is 5 or 0 and then returns the appropriate character. Same rule in all the other roman functions.
    if a==0 or a==5:
        if a==5:
            p = romanNum["b"]
            return p
        else:
            return ""
    #evaluates when the number is 4 or 9 and then returns the appropriate character. 
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
    #evaluates when the number is between 1-3 or 6-8 and then returns the appropriate character. 
    elif a>0 and a<9:
        if a<4:
            p=a*romanNum["a"]
            return p
        else:
            x=(a-5)*romanNum["a"]
            y=romanNum["b"]
            p=y+x
            return p
    #General error handling code
    else:
        return "z1"
        
def romanII(x):
    a=abs(int(x))
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
    a=abs(int(x))
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
    a=abs(int(x))
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
print(negCheck(numX))

