

class Coffee:
    all_coffees = []
    
    def __init__(self, name):
        self.name = name  # Uses the setter
        self._orders = []
        Coffee.all_coffees.append(self)
    
    @property
    def name(self):
        return self._name  # using _name to avoid recursion

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if len(new_name) < 3:
            raise ValueError("Name must be at least 3 characters")
        self._name = new_name
    
    def orders(self):
        return self._orders.copy()  # Return copy to prevent external modification

    def customers(self):
        # unique customers using set comprehension
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:  # Handle case with no orders
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
