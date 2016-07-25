from problem1 import problem1Function
from problem2 import problem2Function
from problem3 import problem3Function
from problem4 import problem4Function

problemNumber = input('Enter a problem number: ') #our input is going to be of type 'string', not the type 'int' which you make expect

if problemNumber == '1':
    print(problem1Function())
if problemNumber == '2':
    print(problem2Function())
if problemNumber == '3':
    print(problem3Function())
if problemNumber == '4':
    print(problem4Function())
    
        
    
    
    



