import ipdb

class Toy:
    
    def __init__(self, size, color = "red"):
        self.size = size
        self.color = color

    def make_sound(self):
        print("I am a toy! Yay!")

    def get_size(self):
        return self._size

    def set_size(self, size_parameter):
        if(type(size_parameter) is str) and (size_parameter in ["small", "medium", "large"]):
            self._size = size_parameter
        else:
            raise ValueError("Size must be a string with the value of small, medium, or large!")
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color_parameter):
        if(type(color_parameter) is str) and (color_parameter in ["red", "blue", "green"]):
            self._color = color_parameter
        else:
            raise ValueError("Color must be a string with the value of red, blue, or green")
    
    size = property(get_size, set_size)

    def __repr__(self):
        return f"Toy object - Size: {self.size}, Color: {self.color}"

toy1 = Toy("medium")
toy2 = Toy("large", "blue")
ipdb.set_trace()