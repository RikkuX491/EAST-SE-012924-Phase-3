import ipdb

class Car:

    all = []
    
    def __init__(self, make, model, year, horn_volume = 1):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume = horn_volume

        Car.all.append(self)

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year_parameter):
        if(isinstance(year_parameter, int)) and (1900 <= year_parameter <= 2023):
            self._year = year_parameter
        else:
            raise ValueError("Year must be an integer and must be between 1900 and 2023!")
    
    @property
    def horn_volume(self):
        return self._horn_volume
    
    @horn_volume.setter
    def horn_volume(self, horn_volume_parameter):
        if(isinstance(horn_volume_parameter, int)):
            self._horn_volume = horn_volume_parameter
        else:
            raise ValueError("Horn volume must be an integer!")
        
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make_parameter):
        if(type(make_parameter) == str) and (len(make_parameter) >= 3):
            self._make = make_parameter
        else:
            raise ValueError("Make must be a string and must be at least 3 characters long!")
        
    def honk_horn(self):
        print(f"BEEP BEEP{'!' * self.horn_volume}")

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model_parameter):
        if(not hasattr(self, 'model')) and (isinstance(model_parameter, str)):
            self._model = model_parameter
        else:
            raise ValueError("Model cannot be changed and must be a string!")
        
    @classmethod
    def average_year(cls):
        # total_year_value = sum([car.year for car in cls.all])
        # return int(total_year_value / len(cls.all))
        list_of_years = [car.year for car in cls.all]
        return int(sum(list_of_years) / len(list_of_years))
        
car1 = Car("Honda", "Odyssey", 2010)
car2 = Car("Toyota", "Camry", 2020, 7)
ipdb.set_trace()