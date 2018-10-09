# -*- coding: utf-8 -*-
"""
Created by xmarkakis on May 3rd, 2018.
This is a script to convert numbers into roman numeral. It really only supports numbers under 1000 and years (up to 5000).
Reason being, roman numerals have weird characters for 5,000 and above. Since I hanve't found a way to insert those special characters,
I just added the lower case values of those characters in the mean time.
"""
romanNum = {"a":"I","b":"V","c":"X","d":"L","e":"C","f":"D","g":"M","h":"v","i":"x"}
romanNum2 ={"1a":"I","1b":"V","1c":"X","2a":"X","2b":"L","2c":"C","3a":"C","3b":"D","3c":"M","4a":"M","4b":"v","4c":"x"}
"""
This is a temp version of the final script. I've overhauling all the code from the original. 
I'm determined to get this script down to a simple few lines. Here are the steps I think the script needs to do:
1. Check if the length of the user input is less than 5 (anything greater than 4 should generate an error)
2. Check if the first character in the string is a negative sign. 
3. Check if the value can be converted into a string. (Look into how this can be done. I'm thinkng a simple if statement that returns true.)
4. Create a function that grans the values and it's index position to evaluate the number independent of the other numbers. 
5. Add the outputs together to generate an accurate roman numeral (need to make sure the "for" loop here evaluates the numbers and adds them in order.)   
"""
numX = input("Enter a number between 1 and 9,999 to convert it into a roman numeral: ")

def negCheck(x):
    if x[:1]=='-':
        m=list(x)
        return checkLen(m[1:])
    else:
        m=list(x)
        return checkLen(m)

def checkLen(x):
    #This function essentially checks the length of the number and then returns the appropriate order of roman numberal function calls based on the length. 
    if len(x)==4:
        #figure out a for loop here to iterate through the string and create the value variable and the index variable. 
        return roman(x[0]) + roman(x[1]) + roman(x[2]) + roman(x[3])   
    elif len(x)==3:
        print(x)
        return romanIII(x[0]) + romanII(x[1]) + romanI(x[2])
    elif len(x)==2:
        print(x)
        return romanII(x[0]) + romanI(x[1])         
    elif len(x)==1:
        if x == 0: 
            print("You entered 0 .... 0 is 0 in roman numerals .... come on!!")
        else:
            return romanI(x)  
    elif len(x)>4:
        print("Nice Try ;-) Please print a value in range")
    else:
        print("Please print a value in range")

def roman(x,y):
    #this will hopefully be the function that will replace romanI through IV
    a=abs(int(x))
    #evaluates when the number is 5 or 0 and then returns the appropriate character. Same rule in all the other roman functions.
    if a==0 or a==5:
        if a==5:
            r = x + y
            p = romanNum2[r]
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
        #case 2 - When the value is zero, need to return the function somehow to the next function
#remember to convert values to int and abs so that you change the string into a value and also get the absolute value as well
print(negCheck(numX))

def var(c):
    for n in var:
        if index position == 1
        return a + n
        else: 
#Create a for loop that evaluates the index as well as the number and returns the dictionary value for the index and value pair. Maybe a while loop as well?
#Treat the "1" in "10,000" as a key intro for the response? So something like "Roman Numeral = "??

