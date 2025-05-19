
class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer 
        self.coffee = coffee      
        self.price = price       
        Order.all_orders.append(self)
        
        # Add to customer and coffee order lists
        customer._orders.append(self)
        coffee._orders.append(self)

    # Price property
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (float, int)):
            raise ValueError("Price must be a number")
        if not 1.0 <= float(new_price) <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(new_price)

    # Coffee property
    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee):
        from coffee import Coffee  # Importing here to avoid circular imports
        if not isinstance(new_coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee Class")
        self._coffee = new_coffee

    # Customer property
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        from customer import Customer  # Importing here to avoid circular imports
        if not isinstance(new_customer, Customer):
            raise ValueError("customer must be an instance of Customer Class")
        self._customer = new_customer
