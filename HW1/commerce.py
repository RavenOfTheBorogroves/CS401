class Product:
    def __init__(self, price, name, avalible):
        self.name = name
        self.price = price
        self.avalible = avalible

    def info(self):
        print("Product name:", self.name)
        print("Product price: $", self.price)
        print("Product Avalible: ",  self.avalible)

class IndoorSport(Product):
    def __init__(self, name, price, avalible):
        super().__init__(price, name, avalible)   # Call parent constructor
        self.category = "Indoor Sports"

    def details(self):
        print(self.name, "is a ", self.category, " item")

class Volleyball(IndoorSport):
    def __init__(self, name, price, avalible,offer):
        super().__init__(price, name, avalible)   # Call parent constructor
        self.Kind = "Vollyball"
        self.offer = offer

    def details(self):
        print(self.name, "is a ", self.category, " item for ", self.Kind) #add more info

class BallforVolley(Volleyball):
    def __init__(self, name, price, avalible, offer, material, size ):
        super().__init__(price, name, avalible, offer)   # Call parent constructor
        self.material = material
        self.size = size 

    def details(self):
        print(self.name, "is a ", self.category, " item for ", self.Kind) #add more info

class VolleyNet(Volleyball):
    def __init__(self, name, price, avalible, offer, type ):
        super().__init__(price, name, avalible, offer)   # Call parent constructor
        self.type = type
        

    def details(self):
        print(self.name, "is a ", self.category, " item for ", self.Kind) #add more info

class TableTennis(IndoorSport):
    def __init__(self, name, price, avalible,offer):
        super().__init__(price, name, avalible)   # Call parent constructor
        self.Kind = "Table Tennis"
        self.offer = offer

    def details(self):
        print(self.name, "is a ", self.category, " item for ", self.Kind) #add more info

    # to do: make a function for checking if there is stock 

class Paddles(TableTennis):
    def __init__(self, name, price, avalible, offer, style):
        super().__init__(price, name, avalible, offer)   # Call parent constructor
        self.style = style
        

    def details(self):
        print(self.name, "is a ", self.category, " item for ", self.Kind) #add more info

class TableBall(TableTennis):
    def __init__(self, name, price, avalible, offer):
        super().__init__(price, name, avalible, offer)   # Call parent constructor

    def details(self):
        print(self.name, "is a ", self.category, " item for ", self.Kind) #add more info

class Table(TableTennis):
    def __init__(self, name, price, avalible, offer, material ):
        super().__init__(price, name, avalible, offer)   # Call parent constructor
        self.material = material
        

    def details(self):
        print(self.name, "is a ", self.category, " item for ", self.Kind) #add more info