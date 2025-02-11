class Fruit: 
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = float(price)

    def details(self): 
        print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~
            Fruit Type: {self.name}
            Fruit Color: {self.color}
            Fruit Cost: {self.price}
            ~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

    def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
        print(f"""
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        Total Cost: {self.name}: {total}
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        """)

apple = Fruit("Apple", "Red", 2)
pear = Fruit("Pear", "Green", 3)
strawberry = Fruit("Strawberry", "Red", 4)

apple.details()
pear.details()
strawberry.details()

apple.calc_sales_tax(.04)
pear.calc_sales_tax(.04)
strawberry.calc_sales_tax(.04)