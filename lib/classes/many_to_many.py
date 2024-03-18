class Hotel:
    
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str)) and (5 <= len(name_parameter) <= 20):
            self._name = name_parameter

    def reviews(self):
        return [review for review in Review.all if review.hotel is self]
    
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
        
class Customer:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name_parameter):
        if(not hasattr(self, 'first_name')) and (isinstance(first_name_parameter, str)) and (len(first_name_parameter) > 0):
            self._first_name = first_name_parameter

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name_parameter):
        if(not hasattr(self, 'last_name')) and (isinstance(last_name_parameter, str)) and (len(last_name_parameter) > 0):
            self._last_name = last_name_parameter

    def reviews(self):
        return [review for review in Review.all if review.customer is self]
    
    def hotels(self):
        return list(set([review.hotel for review in self.reviews()]))
    
    def submit_review(self, hotel, rating, text):
        return Review(hotel, self, rating, text)
    
    def hotel_names(self):
        if(len(self.reviews()) == 0):
            return None
        else:
            return [hotel.name for hotel in self.hotels()]
        
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
        if(isinstance(hotel_parameter, Hotel)):
            self._hotel = hotel_parameter

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer_parameter):
        if(isinstance(customer_parameter, Customer)):
            self._customer = customer_parameter