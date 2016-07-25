#Write a program that asks the user for her name and greets her with her name.
def problem3Function():
    problemDescription = 'Description: Write a program that asks the user for her name and greets her with her name.'
    print(problemDescription) 
    

    userName = input('What is your name?: ')
    greeting = 'Hello ' + userName + '!'
    
    return greeting
    