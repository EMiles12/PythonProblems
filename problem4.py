#Modify the previous program such that only the users Alice and Bob are greeted with their names.
def problem4Function():
    problemDescription = 'Description: Modify the previous program such that only the users Alice and Bob are greeted with their names.'
    print(problemDescription)
    userName = input('What is your name?: ')
    if userName == 'Alice' or userName == 'Bob':    
        greeting = 'Hello ' + userName + '!'
        return greeting
        
    else:
        greeting = 'You\'re not Alice or Bob! Go back to your cave, peasant!'
        return greeting
        
    
    
    
    

    