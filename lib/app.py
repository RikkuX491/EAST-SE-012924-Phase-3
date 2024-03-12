import ipdb

# Deliverable 1
def combine_sequences(seq1, seq2):
    return seq1 + seq2

# Deliverable 2
def sequence_n_times(seq, n):
    return seq * n

# Deliverable 3
def average(seq):
    return sum(seq) / len(seq)

# Deliverable 4
def append_n_times(input_list, element, n):
    for i in range(n):
        input_list.append(element)
    return input_list

foods = [
    {
        "name": "Flatburger",
        "price": 10.99
    },
    {
        "name": "French Fries",
        "price": 1.99
    },
    {
        "name": "Burrito",
        "price": 7.99
    }
]

# Deliverable 5
food_names = [food['name'] for food in foods]

# Deliverable 6
food_prices = [food['price'] for food in foods]
average_price = sum(food_prices) / len(food_prices)

animals = [
    {
        "name": "Fido",
        "animal_type": "Dog"
    },
    {
        "name": "Kitty",
        "animal_type": "Cat"
    },
    {
        "name": "Fluffy",
        "animal_type": "Guinea Pig"
    }
]

# Deliverable 7
animal_descriptions = [f"{animal['name']} is a {animal['animal_type']}" for animal in animals]