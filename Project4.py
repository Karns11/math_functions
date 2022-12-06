###########################################################
#
#  CSE 231 project #4
#
#  function to check if a string can be converted to a float.
#  function to calculate approximated value of the factorial of a given
#  integer.
#  function to calculate an approximated value of e.
#  function to calculate an an approximated value of pi.
#  fuction to calculate an approximated value of sinh of given radians.
#  a final function that includes the main body of code where we will
#  interact with the user.
#  display closing message.
#  
#    
###########################################################

import math
EPSILON = 0.0000001 

#menu options definitions
MENU = '''\nOptions below:
    ‘F’: Factorial of N.
    ‘E’: Approximate value of e.
    ‘P’: Approximate value of Pi.
    ‘S’: Approximate value of the sinh of X.
    ‘M’: Display the menu of options.
    ‘X’: Exit.
'''

#float check function to determine if a given input can be conerted to float
def float_check(num):
    ''' check if a given input is a float or not
    num: what we are checking
    returns: true if it is a float, false otherwise''' 
    dot_number = num.count('.')
    if dot_number > 1:
        return False
    elif dot_number == 1:
        num = num.replace('.', '1')
        return num.isdigit()
    else:
        return num.isdigit()

def factorial(N): 
    ''' compute the factorial of a given input
    N: number to be processed(str)
    returns: the computed factorial (int or None)''' 
    n_int = int(N)
    factorial = 1 #define factorial variable
    if n_int == 0: #factorial of 0 is 1
        return 1
    elif n_int < 0: #cannot compute negative factorial
        return None
    for num in range(1, n_int+1):
        factorial = factorial * num #factorial calculation
    return factorial
 
def e(): 
    ''' compute estimated value of e
    parameters: None
    returns: estimated value of e (float) ''' 
    term = 1
    approx_e_sum = 0
    n = 0
    while abs(term) > 0.0000001:
        approx_e_sum = approx_e_sum + term
        n += 1
        term = (1/factorial(n))
    return round(approx_e_sum, 10) #return final calculation

def pi():
    ''' compute estimated value of pi
    parameters: None
    returns: calculated value of pi (Float) ''' 
    pi_term = 1 #define the term variable
    approx_pi_sum = 0 #assign the sum variable to 0
    m = 0 #increment variable
    while abs(pi_term) > 0.0000001: #epsilon
        approx_pi_sum = approx_pi_sum + pi_term
        m += 1
        pi_term = ((-1)**m)/((2*m)+1) #calculate each term to be added to sum
    return 4 * round(approx_pi_sum, 10) #multiply the sum by 4 after calculations

def sinh(x): 
    ''' comoute sinh of a given string
    parameters: what we are going to compute(String)
    returns: computed value of sinh (Float or None) ''' 
    #if we receive a value error, dont error out, just return none
    try:
        x_flt = float(x)
    except ValueError:
        return None
    sinh_term = x_flt #define term variable
    approx_sinh_val = 0 #define end variable
    num = 0 #increment variable
    while abs(sinh_term) > 0.0000001: #epsilon
        approx_sinh_val = approx_sinh_val + sinh_term
        num += 1
        # main sinh calculation
        sinh_term = ((x_flt)**((2*num)+1))/(factorial((2*num)+1))
    return round(approx_sinh_val, 10)  #return final calculation

#main function to interact with user
def main(): 
    ''' main function to interact with user
    parameters: None
    returns: Nothing'''
    print(MENU)
    prompt = input("\nChoose an option: ")
    prompt_lower = prompt.lower() #convert prompt to lower for while loop
    while prompt_lower != 'x': #x will exit while loop
        if prompt_lower == 'f':
            print("\nFactorial")
            integer_prompt = input("Input non-negative integer N: ")
            #if the input is not a float, print error message
            if float_check(integer_prompt) == False:
                print("\nInvalid N.")
            #otherwise, continue as normal
            else:
                integer_prompt_conv = float(integer_prompt)
                #if the float is negative, print error message
                if integer_prompt_conv < 0:
                    print("\nInvalid N.")
                #otherwise continue as normal
                else:
                    calc_f = factorial(integer_prompt)
                    #grab factorial function for printing
                    print("\nCalculated:", calc_f)
                    #grab math function for printing
                    math_f = math.factorial(integer_prompt_conv)
                    print("Math:", round(math_f, 10))
                    #subtract the difference and take the absolute value
                    difference_f = abs(calc_f) - abs(math_f)
                    print("Diff: {}".format(difference_f)) #dont round here
        elif prompt_lower == 'e':
            print('\ne')
            calc_e = e()
            #grab e function for printing
            print("Calculated:", calc_e)
            math_e = round(math.e, 10)
            #grab math e function for printing
            print("Math:", round(math_e, 10))
            #subtract the difference and take absolute value
            difference_e = abs(math_e - calc_e)
            print("Diff: {:.10f}".format(difference_e)) #round to 10 decimals
        elif prompt_lower == 'p':
            print('\npi')
            calc_pi = pi()
            #grab pi function for printing
            print("Calculated:", calc_pi)
            math_pi = math.pi
            #grab math pi function for printing
            print("Math:", round(math_pi, 10))
            #subtract the difference and take absolute value
            difference_pi = abs(math_pi - calc_pi)
            print("Diff: {:.10f}".format(difference_pi)) #round to 10 decimals
        elif prompt_lower == 's':
            print("\nsinh")
            radian_prompt = input("X in radians: ")
            #if input is not a flaot, print error message
            if float_check(radian_prompt) == False:
                print("\nInvalid X.")
            #otherwise, continue as normal
            else:
                radian_prompt_conv = float(radian_prompt)
                calc_s = sinh(radian_prompt)
                #grab sinh function for printing
                print("\nCalculated:", calc_s)
                #grab math.sinh function for printing
                math_s = math.sinh(radian_prompt_conv)
                print("Math:", round(math_s, 10))
                #subtract the difference and take the absolute value
                difference_s = abs(math_s - calc_s)
                print("Diff: {:.10f}".format(difference_s)) #round to 10 decimals
        # if the user selects m, print the menu options
        elif prompt_lower == 'm':
            print(MENU)
        else:
            #if anything else is entered, print what was entered, and an error message
            print("\nInvalid option:", prompt_lower.upper())
            print(MENU)
        prompt = input("\nChoose an option: ") #repeat the prompt until x is entered
        prompt_lower = prompt.lower()
    print("\nThank you for playing.") #print thank you message

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == '__main__': 
    main()
