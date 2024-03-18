#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Hotel
from classes.many_to_many import Customer
from classes.many_to_many import Review

if __name__ == '__main__':
    # don't remove this line, it's for debugging!
    
    hotel1 = Hotel("Marriott")
    hotel2 = Hotel("Hampton Inn")

    customer1 = Customer("Alice", "Baker")
    customer2 = Customer("Bob", "Smith")

    review1 = Review(hotel1, customer1, 5, "Best Hotel ever!")
    review2 = Review(hotel1, customer2, 4, "Great amenities here at this hotel!")
    review3 = Review(hotel2, customer1, 2, "Not such a good experience here...")
    review4 = Review(hotel1, customer1, 3, "Not as good as my last experience here.")
    
    ipdb.set_trace()