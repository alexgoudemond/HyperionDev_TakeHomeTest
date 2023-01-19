'''
Author: Alexander Goudemond
Date Created: 2023/01/19

This code contains the code to verify and work with ISBN-10 and ISBN-13 numbers
'''

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------Sanitise and Parse Input
#--------------------------------------------------------------------------------------------------------------

def validateInputLength(userInput, desiredLength1, desiredLength2):
    while (len(userInput) != desiredLength1 and len(userInput) != desiredLength2):
        userInput = input("Please enter a number that contains either \'" + str(desiredLength1) + "\' or \'" + str(desiredLength2) + "\' characters: ")
    return userInput

# check each digit is valid
def ensureIsbnDigits(userInput, desiredLength1, desiredLength2):
    userInput = validateInputLength(userInput, desiredLength1, desiredLength2)
    userInput = userInput.upper() # uppercase, to ignore case for 'X'
    
    validInput = True

    while (True):
        validInput = True

        for i in range(len(userInput)):
            # valid final char
            if (i == len(userInput)-1 and userInput[i] == 'X'):
                continue
            if (ord(userInput[i]) < ord("0") or ord(userInput[i]) > ord("9") ):
                validInput = False; break
        
        if (not validInput):
            print("Invalid code entered. All characters should be digits, unless the final character is \'X\'")
            userInput = validateInputLength("", desiredLength1, desiredLength2)
            userInput = userInput.upper() # uppercase, to ignore case for 'X'
        else:
            break
    
    return userInput      

#--------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------Verify and Convert ISBN codes
#--------------------------------------------------------------------------------------------------------------

# follow rule for checking ISBN-10
def isbn10Algorithm(number):
    startingNum = 10
    answer = 0

    for digit in number:
        if (digit == "X"):
            answer += 10 * startingNum

        answer += int(digit) * startingNum
        startingNum -= 1
    
    return answer

# follow rule for checking ISBN-13
def isbn13Algorithm(number):
    multiple = -1
    answer = 0

    for i in range(len(number)):
        if (i % 2 == 0):    multiple = 1
        else:               multiple = 3

        if (number[i] == "X"):
            answer += 10 * multiple

        answer += int(number[i]) * multiple
    
    return answer


def checkIsbn10(number):
    if (len(number) != 10):
        return "Invalid"

    answer = isbn10Algorithm(number)

    if (answer % 11 == 0):
        return "Valid"
    else:
        return "Invalid"

# ensure handle conversion to isbn-13 where necessary
def checkIsbn13(number):
    if (len(number) == 10):
        number = convertIsbn10ToIsbn13(number)
    elif (len(number) != 13):
        return "Invalid"
        
    answer = isbn13Algorithm(number)
        
    if (answer % 10 == 0):
        return "Valid"
    else:
        return "Invalid"


'''
Trick here is to calculate ISBN-13 as per normal, BUT, the final digit is
decided by the 'roof' of the incomplete sum!
i.e. 9780316066524 --> 978031606652_                                    # Ignore the last digit
                   --> 9 + 21 + 8 + 0 + 3 + 3 + 6 + 0 + 6 + 18 + 5 + 6  # Follow the ISBN-13 algorithm
                   --> sum is 85
                   --> roof(85) == 90                                   # algorithm divides by 10
                   --> 90 - 85 == 5, therefore the final digit should be 5
     
'''
def convertIsbn10ToIsbn13(number):
    # if (checkIsbn10(number) == "Invalid"):
    #     print("Original Number to is not a Valid ISBN-10 code")
    
    # print("Original Number: ", number)
    
    # modify number
    number = "978" + number[0 : -1]

    answer = isbn13Algorithm(number)
    
    # Apply logic for last digit
    if (answer % 10 == 0):
        finalDigit = 0
    else:
        finalDigit = 10 - int(str(answer)[-1]) # isolate final digit using String indexing
    
    # print("Answer:", answer)
    # print("Final Digit:", finalDigit)

    number += str(finalDigit)

    # print("New Number:      ", number)
    
    return number   

#--------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------Test case Functions
#--------------------------------------------------------------------------------------------------------------

def evalIsbn10(number):
    if (len(number)  != 10):
        return "Invalid length"

    startingNum = 10
    answerString = ""

    for digit in number:
        if (digit == "X"):
            answerString += "10 * " + str(startingNum)

        answerString += digit + " * " + str(startingNum)
        startingNum -= 1

        answerString += " + "
    
    return answerString[0 : -3] # remove last 3 symbols

def evalIsbn13(number):   
    if (len(number) == 10):
        number = convertIsbn10ToIsbn13(number)
    elif (len(number) != 13):
        return "Invalid"

    multiple = -1
    answerString = ""

    for i in range(len(number)):
        if (i % 2 == 0):    multiple = 1
        else:               multiple = 3

        if (number[i] == "X"):
            answerString += "10 * " + str(multiple)

        answerString += number[i] + " * " + str(multiple)
    
        answerString += " + "
    
    return answerString[0 : -3]

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------Main Program Below
#--------------------------------------------------------------------------------------------------------------

def isbn13(number):

    if (len(number) == 13):
        return checkIsbn13(number)
    
    elif (len(number) == 10):
        answer = checkIsbn10(number)

        if (answer == "Invalid"): return answer

        # if ISBN-10 is valid, convert to ISBN-13
        else: return convertIsbn10ToIsbn13(number)


print("\nWelcome! This program will verify and work with ISBN-10 and ISBN-13 codes")
print("To begin, please enter a code below. To terminate the program, please enter the sequence \"End\"")

userInput = input("\nPlease enter a number: ")

while (userInput.lower() != "end"):
    # sanitise and parse number
    userInput = validateInputLength(userInput, 10, 13)
    userInput = ensureIsbnDigits(userInput, 10, 13)

    # determine if valid!
    print(isbn13(userInput))

    # uncomment below if you wish to run the test cases to show the logic
    '''
    print("\nEvaluations shown below:")

    if (len(userInput) == 13):
        print("ISBN-13")
        print(evalIsbn13(userInput), "==", isbn13Algorithm(userInput), "-->", checkIsbn13(userInput))

            
    elif (len(userInput) == 10):
        answer = checkIsbn10(userInput)
        print("ISBN-10")
        print(evalIsbn10(userInput), "==", isbn10Algorithm(userInput), "-->", answer)

        if (answer == "Valid"): 
            print("ISBN-10 Converted to ISBN-10")
            print(evalIsbn13(userInput), "==", isbn13Algorithm( convertIsbn10ToIsbn13(userInput) ), end=" ") # convert for algorithm necessary just for testing
            print("-->", checkIsbn13(userInput))
    '''

    userInput = input("\nPlease enter a number: ")

print("\nProgram complete, Thank you!\n")