import ipdb

# List
fruits = [
    {
        'name': "Apple",
        'price': 3.99
    },
    {
        'name': "Banana",
        'price': 0.99
    },
    {
        'name': "Strawberry",
        'price': 1.99
    }
]
# print(fruits)

foods = ['pasta', 'seafood', 'pasta']
# print(foods)

# Tuple
# countries = ('Spain',)
countries = ('Spain', 'France')
# print(countries)

# String
word = "Good Morning!"
# print(word)

# ipdb.set_trace()

# Dictionary
person = {
    'name': 'Alice',
    'age': 23
}
# print(person)

# Set
set_of_hobbies = {'Jogging', 'Swimming', 'Ice Skating', 'Swimming'}
# list_of_same_hobbies = list(set_of_hobbies)
# print(set_of_hobbies)
# print(list_of_same_hobbies)

# List Comprehension
list_of_fruit_names = [fruit['name'] for fruit in fruits]
list_of_fruit_prices = [fruit['price'] for fruit in fruits]
list_of_cheap_fruit_names = [fruit['name'] for fruit in fruits if fruit['price'] < 1]

# Generator Expression
generator_expression_fruit_names = (fruit['name'] for fruit in fruits)

ipdb.set_trace()