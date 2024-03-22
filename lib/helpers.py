from models.hotel import Hotel
from models.customer import Customer
from models.review import Review

def initialize_database():
    Hotel.create_table()
    Customer.create_table()
    Review.create_table()

    Hotel.get_all()
    Customer.get_all()
    Review.get_all()

def menu():
    print("\nHere's the main menu!")
    print("h: Interact with Hotel data")
    print("c: Interact with Customer data")
    print("r: Interact with Review data")
    print("q: Quit the program\n")

def exit_program():
    print("Goodbye!\n")
    quit()

def interact_with_hotel_data():
    while(True):
        hotel_options_menu()
        user_input = input("Select an option from the menu: ")
        if(user_input == 'c'):
            print("Create a new hotel")
            break
        elif(user_input == 'r'):
            retrieve_hotels()
            break
        elif(user_input == 'u'):
            print("Update a hotel")
            break
        elif(user_input == 'd'):
            print("Delete a hotel")
            break
        else:
            print("Invalid input! Please try again!\n")

def interact_with_customer_data():
    print("You are now interacting with the Customer data!")

def interact_with_review_data():
    print("You are now interacting with the Review data!")

def hotel_options_menu():
    print("\nHere's the Hotel options menu!")
    print("c: Create a new hotel")
    print("r: Retrieve hotel data")
    print("u: Update a hotel")
    print("d: Delete a hotel\n")

def retrieve_hotels():
    options_for_retrieve_hotels()
    user_input = input("Select an option from the menu: ")

    while(True):
        if(user_input == 'a'):
            print("\nHere are all of the hotels:")
            for hotel in Hotel.all:
                print(hotel)
            # User can press 'return' to continue...
            user_input = input("\nPress 'return' to continue...")
            break
        elif(user_input == '1'):
            while(True):
                try:
                    user_input = input("\nEnter a number for the hotel id to search: ")
                    user_input = int(user_input)
                    hotel = Hotel.find_by_id(user_input)
                    if(hotel):
                        print("\nHere is the hotel you requested:")
                        print(Hotel.find_by_id(user_input))
                    else:
                        print("\nHotel Not Found!")
                    user_input = input("\nPress 'return' to continue...")
                    break
                except:
                    print("Invalid input! Please try again!")
            break
        else:
            print("Invalid input! Please try again!\n")

def options_for_retrieve_hotels():
    print("\nWould you like to retrieve all hotels or just one?")
    print("a: Retrieve all hotels")
    print("1: Retrieve 1 hotel\n")