from models.__init__ import CONN, CURSOR

class Review:

    all = []
    
    def __init__(self, hotel, customer, rating, text):
        self.hotel = hotel
        self.customer = customer
        self.rating = rating
        self.text = text

        Review.all.append(self)

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating_parameter):
        if(not hasattr(self, 'rating')) and (isinstance(rating_parameter, int)) and (1 <= rating_parameter <= 5):
            self._rating = rating_parameter

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text_parameter):
        if(not hasattr(self, 'text')) and (isinstance(text_parameter, str)) and (3 <= len(text_parameter) <= 40):
            self._text = text_parameter

    @property
    def hotel(self):
        return self._hotel
    
    @hotel.setter
    def hotel(self, hotel_parameter):
        from models.hotel import Hotel
        if(isinstance(hotel_parameter, Hotel)):
            self._hotel = hotel_parameter

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer_parameter):
        from models.customer import Customer
        if(isinstance(customer_parameter, Customer)):
            self._customer = customer_parameter