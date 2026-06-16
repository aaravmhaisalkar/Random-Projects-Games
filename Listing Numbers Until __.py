from Functions import number_until_x  
from Functions import convert_list_to_string  
x = input("Please enter a number:\n")
convertInput = input("Should the list be conveted to a string?(y/n)\n")
result = number_until_x(int(x))
convertedResult = convert_list_to_string(result)

if convertInput == "y":
    print(f'The given list from 0 to {x} is: {convertedResult}')
elif convertInput == "n":
    print(f'The given string from 0 to {x} is: {result}')
else:
    print("idk how u got here, the code is bugged")
