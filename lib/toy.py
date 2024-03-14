import ipdb

class Toy:

    all = []
    
    def __init__(self, size, nickname, color = "red", hello = "hi"):
        self.size = size
        self.color = color
        self.nickname = nickname
        self.hello = hello

        if(len(Toy.all) == 0):
            self.id = 1
        else:
            self.id = Toy.all[-1].id + 1

        Toy.all.append(self)

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

    @property
    def nickname(self):
        return self._nickname
    
    @nickname.setter
    def nickname(self, nickname_parameter):
        if(not hasattr(self, 'nickname')):
            self._nickname = nickname_parameter
        else:
            raise Exception('Cannot change the nickname for a Toy!')
        
    @classmethod
    def get_toy_nicknames(cls):
        toy_nicknames = [toy.nickname for toy in cls.all]
        return toy_nicknames

    def __repr__(self):
        return f"Toy # {self.id} - Size: {self.size}, Nickname: {self.nickname}, Color: {self.color}"

toy1 = Toy("medium", "Woody")
toy2 = Toy("large", "Buzz Lightyear", "blue")
ipdb.set_trace()