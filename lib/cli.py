from helpers import *

if __name__ == '__main__':

    initialize_database()
    
    while(True):
        menu()
        user_input = input("Select an option from the menu: ")
        if(user_input == 'q'):
            exit_program()
        elif(user_input == 'h'):
            interact_with_hotel_data()
        elif(user_input == 'c'):
            interact_with_customer_data()
        elif(user_input == 'r'):
            interact_with_review_data()
        else:
            print("Invalid input! Please try again!\n")