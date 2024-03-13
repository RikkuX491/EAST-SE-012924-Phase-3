import ipdb

class Toy:
    
    def __init__(self, size, color = "red"):
        self.size = size
        self.color = color
        # print(f"Congratulations! You created a new Toy: {self}")
        # print(f"Your toy's size will be {size}")

    def make_sound(self):
        print("I am a toy! Yay!")

    def get_size(self):
        # print("Getting the size...")
        return self._size

    def set_size(self, size_parameter):
        # print("Setting the size...")
        if(type(size_parameter) is str) and (size_parameter in ["small", "medium", "large"]):
            self._size = size_parameter
        else:
            raise ValueError("Size must be a string with the value of small, medium, or large!")
        
    @property
    def color(self):
        # print("Getting the color...")
        return self._color
    
    @color.setter
    def color(self, color_parameter):
        # print("Setting the color...")
        if(type(color_parameter) is str) and (color_parameter in ["red", "blue", "green"]):
            self._color = color_parameter
        else:
            raise ValueError("Color must be a string with the value of red, blue, or green")
    
    size = property(get_size, set_size)
    # color = property(get_color, set_color)

    def __repr__(self):
        return f"Toy object - Size: {self.size}, Color: {self.color}"

toy1 = Toy("medium")
toy2 = Toy("large", "blue")
ipdb.set_trace()