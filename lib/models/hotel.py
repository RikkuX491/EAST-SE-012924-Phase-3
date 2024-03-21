from models.__init__ import CONN, CURSOR

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
        from models.review import Review
        return [review for review in Review.all if review.hotel is self]
    
    def customers(self):
        return list(set([review.customer for review in self.reviews()]))