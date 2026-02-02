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

class OutdoorSport(Product):
    def __init__(self, name, price, avalible):
        super().__init__(price, name, avalible)   # Call parent constructor
        self.category = "Outdoor Sports"

    def details(self):
        print(self.name, "is a ", self.category, " item")

class Camping(OutdoorSport):
    def __init__(self, name, price, avalible):
        super().__init__(price, name, avalible)   # Call parent constructor

    def details(self):
        print(self.name, "is a ", self.category, " item")

class Tent(Camping):
    def __init__(self, name, price, avalible,size, durability, weather):
        super().__init__(price, name, avalible)   # Call parent constructor
        self.size = size
        self.durability =durability
        self.weather = weather 

    def details(self):
        print(self.name, "is a ", self.category, " item")

class Soccer(OutdoorSport):
    def __init__(self, name, price, avalible, players):
        super().__init__(price, name, avalible)   # Call parent constructor
        self.players =players
        self.discount = .05
        self.totalcost = self.price
    
    def discount(self):
        self.totalcost = self.price - (self.players * self.discount * self.price)

    def details(self):
        print(self.name, "is a ", self.category, " item")


class soccerBall(Soccer):
    def __init__(self, name, price, avalible, players,material):
        super().__init__(price, name, avalible,players)   # Call parent constructor
        self.material =material

    def details(self):
        print(self.name, "is a ", self.category, " item") #add more 

class soccerNet(Soccer):
    def __init__(self, name, price, avalible, players, size):
        super().__init__(price, name, avalible,players)   # Call parent constructor
        self.size =size

    def details(self):
        print(self.name, "is a ", self.category, " item") #add more 

#add user interaction
# ill create functions to check if user input is correct ie if int imput needed the input is an int 
# create functions for int string float also 
# found a thing about rounding float to decimals 
# 'Your Meal Price is %.2f' %  mealPrice 
#will use this for price 








# sources:
# https://www.geeksforgeeks.org/python/python-oops-concepts/
# https://www.geeksforgeeks.org/python/inheritance-in-python/
# https://stackoverflow.com/questions/3221654/specifying-number-of-decimal-places-in-python