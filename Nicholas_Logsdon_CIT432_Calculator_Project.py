#Nicholas Logsdon
#CIT 486
#Mark Revels
#04/11/2021
#import math libray to gain access to sqrt fuction
import math
#This was the only native sloution I could find for copying to clipboard
from subprocess import check_call
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)
#creating methods for each requested computation
def addtn(float1, float2):
    total = float1 + float2
    return(total)

def subtrct (float1, float2):
    difference = float1 - float2  
    return(difference)

def multpl(float1, float2):
    product = float1 * float2
    return(product)

def divid(float1, float2):
    quotient = float1 / float2
    return(quotient)

def squareroot(float1):
    square_root = math.sqrt(float1)
    return(square_root)

#begin logic for actual calculator
def main ():
    #define the first sentinel for wanting to keep running calculations on the calculator
    control = ''
    while control != 'E':
        inner_control = ' '
        #gather a float from the user for the first equation in any primary sentinel loop
        float1 = float(input('Enter the first number: '))
        #start a second sentinel loop if further calculations wish to be ran on the result of the first equation until user is satisfied
        while inner_control != 'N':
            #gather a operation from the user input validation is handled in the if-elif-else statements to follow
            operator = input('Enter + for addition, - for subtraction,\
 * for multiplication / for division, or sqrt for square root: ')
            #gather the second float for the first loop or the next number using on the result of the previous loop added try except validation to prevent user from not entering a number even if not evaluated
            while True:
                try:
                    float2 = float(input('Enter the second number if doing square root enter any number to continue: '))
                except ValueError:
                    print('please enter a number')
                else:
                    break
            #input validation loop for operator
            while operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != 'sqrt':
                operator = input('invalid operator, please input a valid operator: ')
            #if-elif statements to determine which operation to perform
            if operator == '+':
                float3 = addtn(float1, float2)
            elif operator == '-':
                float3 = subtrct(float1, float2)
            elif operator == '*':
                float3 = multpl(float1, float2)
            elif operator == '/':
                #input validation loop to prevent divide by 0 issues
                while float2 == 0:
                    print('divide by 0 error')
                    float2 = float(input('please enter a different divisor: '))
                float3 = divid(float1, float2)
            elif operator == 'sqrt':
                #input validation loop to prevent negative square root issues
                while float1 < 0:
                    print('Error number for square root must be positive')
                    float1 = float(input('please enter another number to squareroot: '))
                float3 = squareroot(float1)
            #shows result of calculation and copys to operating system clipboard by referencing previous method
            print(float3)
            copy2clip(str(float3))
            #sets float1 to float3 if further calculations need to be ran on the result of the current loop
            float1 = float3
            #prompts user for sentinel to end running calculations on current result
            inner_control = input('Would you like to make further calculations press N for no or anything else to make further calculations on this number: ').upper()
        #prompts user on sentinel to exit calculator or run different calculations    
        control = input('enter e to exit or simply hit enter to keep running calculations: ').upper()
#calls calculator
main()
