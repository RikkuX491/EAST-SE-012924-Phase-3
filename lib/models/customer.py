from models.__init__ import CONN, CURSOR

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
        from models.review import Review
        return [review for review in Review.all if review.customer is self]
    
    def hotels(self):
        return list(set([review.hotel for review in self.reviews()]))
    
    # add new ORM methods after existing methods