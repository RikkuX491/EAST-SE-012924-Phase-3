# One-to-many: 1 Hotel (instance) has many Reviews (many review instances)
class Hotel:

    all = []
    
    def __init__(self, name):
        self.name = name

        if(len(Hotel.all) == 0):
            self.id = 1
        else:
            self.id = Hotel.all[-1].id + 1

        Hotel.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str)) and (5 <= len(name_parameter) <= 20):
            self._name = name_parameter

    def reviews(self):
        return [review for review in Review.all if review.hotel is self]
    
    # Many-to-many: 1 Hotel has many Customers and 1 Customer has many Hotels,
    # creating the many-to-many relationship between Hotel and Customer (through Review)

    # In this example, we can retrieve the data for the hotel's customers
    def customers(self):
        return list(set([review.customer for review in self.reviews()]))
    
    def review_texts(self):
        if(len(self.reviews()) == 0):
            return None
        else:
            return [review.text for review in self.reviews()]
        
    def average_rating(self):
        if(len(self.reviews()) == 0):
            return None
        else:
            ratings_list = [review.rating for review in self.reviews()]
            return sum(ratings_list) / len(ratings_list)
        
    def customers_more_than_three_reviews(self):
        list_more_than_three = [customer for customer in self.customers() if len([review for review in customer.reviews() if review.hotel is self]) > 3]
        if(len(list_more_than_three) == 0):
            return None
        else:
            return list_more_than_three
        
    def __repr__(self):
        return f"<Hotel # {self.id} => Name: {self.name}>"

class Customer:

    all = []
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        if(len(Customer.all) == 0):
            self.id = 1
        else:
            self.id = Customer.all[-1].id + 1

        Customer.all.append(self)

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name_parameter):
        if(not hasattr(self, 'first_name')) and (isinstance(first_name_parameter, str)) and (len(first_name_parameter) > 0):
            self._first_name = first_name_parameter
        else:
            raise Exception("First name cannot be changed and must be a string greater than 0 characters long!")
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name_parameter):
        if(not hasattr(self, 'last_name')) and (isinstance(last_name_parameter, str)) and (len(last_name_parameter) > 0):
            self._last_name = last_name_parameter
        else:
            raise Exception("Last name cannot be changed and must be a string greater than 0 characters long!")
        
    def reviews(self):
        return [review for review in Review.all if review.customer is self]
    
    # Many-to-many: 1 Hotel has many Customers and 1 Customer has many Hotels,
    # creating the many-to-many relationship between Hotel and Customer (through Review)
    
    # In this example, we can retrieve the data for the customer's hotels
    def hotels(self):
        return list(set([review.hotel for review in self.reviews()]))
    
    def submit_review(self, hotel, rating, text):
        return Review(hotel, self, rating, text)
    
    def hotel_names(self):
        if(len(self.reviews()) == 0):
            return None
        else:
            return [hotel.name for hotel in self.hotels()]
        
    def __repr__(self):
        return f"<Customer # {self.id} => First Name: {self.first_name}, Last Name: {self.last_name}>"

# Belongs to: Each Review belongs to 1 Hotel
class Review:

    all = []
    
    def __init__(self, hotel, customer, rating, text):
        self.hotel = hotel
        self.customer = customer
        self.rating = rating
        self.text = text

        if(len(Review.all) == 0):
            self.id = 1
        else:
            self.id = Review.all[-1].id + 1

        Review.all.append(self)

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating_parameter):
        if(not hasattr(self, 'rating')) and (isinstance(rating_parameter, int)) and (1 <= rating_parameter <= 5):
            self._rating = rating_parameter
        else:
            raise Exception("Rating cannot be changed and must be an integer between 1 and 5!")
        
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text_parameter):
        if(not hasattr(self, 'text')) and (isinstance(text_parameter, str)) and (3 <= len(text_parameter) <= 40):
            self._text = text_parameter
        else:
            raise Exception("Text cannot be changed and must be between 3 and 40 characters long!")

    @property
    def hotel(self):
        return self._hotel
    
    @hotel.setter
    def hotel(self, hotel_parameter):
        if(isinstance(hotel_parameter, Hotel)):
            self._hotel = hotel_parameter
        else:
            raise Exception("Hotel must be a hotel instance!")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer_parameter):
        if(isinstance(customer_parameter, Customer)):
            self._customer = customer_parameter
        else:
            raise Exception("Customer must be a customer instance!")
        
    def __repr__(self):
        return f"<Review # {self.id} => Rating: {self.rating}, Text: {self.text}, {self.hotel}, {self.customer}>"