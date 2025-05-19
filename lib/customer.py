from coffee import Coffee
from order import Order
class Customer:
    all_customers = []
    
    def __init__(self, name):
        self.name = name  # Uses the setter
        self._orders = []
        Customer.all_customers.append(self)
    
    @property
    def name(self):
        return self._name  # using _name to avoid recursion

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(new_name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = new_name
    
    def orders(self):
        return self._orders.copy()  # return a copy to prevent external modification

    def coffees(self):
        # return unique coffees using set comprehension
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee")
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee")
        
        if not coffee.orders():
            return None
        
        customer_spending = {}
        for order in coffee.orders():
            if order.customer in customer_spending:
                customer_spending[order.customer] += order.price
            else:
                customer_spending[order.customer] = order.price
        
        return max(customer_spending.items(), key=lambda item: item[1])[0]