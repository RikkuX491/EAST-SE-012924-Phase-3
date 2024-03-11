import ipdb

# print("Greetings! Welcome to Python!")

# status = "hungry"

# if(status == "sleepy"):
#     print("I'm so sleepy...")
# elif(status == "energetic"):
#     print("I'm so energetic!")
# else:
#     print("I'm just chilling out.")

number = 4.5
# if(typeof number == 'number' || typeof number == 'string')
# if(type(number) in [int, float]) and number > 0:
#     word = "Cake"
    # print("It's a valid number")
    # ipdb.set_trace()
# elif(type(number) == float):
#     print("It's a float!")
# else:
#     raise Exception
    # raise Exception('Invalid value!')

# Ternary statement
result = "It's a valid number!" if ((type(number) in [int, float]) and number > 0) else "Invalid value!"
# print(result)

# for index in range(1, 11):
#     print(index)

fruit_list = ['apple', 'orange', 'banana']
# for fruit in fruit_list:
#     print(fruit)

index = 0
while(index < len(fruit_list)):
    # print(fruit_list[index])
    index += 1

def print_hi():
    print('Hi!') # side-effect of this function

# return_value = print_hi()
# print(return_value)
    
def combine_strings(str1, str2):
    return str1 + str2

word1 = "apple"
word2 = "sauce"
string_result = combine_strings(word1, word2)
# print(string_result)

number1 = 3
number2 = 1

try:
    quotient = number1 / number2
except:
    print("Sorry! You can't divide by zero!")

print('Yay! We were able to handle the error and continue running our code!')
print("The End")