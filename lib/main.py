from coffee import Coffee
from customer import Customer
from order import Order


try:
    # valid orders

    brian = Customer("Brian")
    blackcoffee = Coffee("Black coffee")
    order1 = Order(brian, blackcoffee, 7.0)

    edwin = Customer("Edwin")
    strongtea = Coffee("Strong tea")
    order2= Order(edwin, strongtea, 6.5)

    order3= Order(brian, blackcoffee, 7.0)

    biggest_spender=Customer.most_aficionado(blackcoffee)

    print(f"Biggest spender on black coffee: {biggest_spender.name}")

    #all coffee instances
    print("********All cofffees*********")
    for coffee in Coffee.all_coffees:
     print(coffee.name)


    #all customers instances
    print("********All Customers*********")
    for customer in Customer.all_customers:
     print(customer.name)


    #all orders instances
    print("**********All Orders***********")
    for order in Order.all_orders:
     print(f"Name:{order.customer.name}| {order.coffee.name} | Price:{order.price}")



    espresso = Coffee("Espresso")
    mary = Customer("mary")

    # mary orders an espresso
    order1 = mary.create_order(espresso, 4.50)

    # Check associations
    print(espresso.orders())     # [order1]
    print(espresso.customers())  # [mary]
    print(mary.orders())        # [order1]
    print(mary.coffees())       # [espresso]
    print(order1.customer)       # mary
    print(order1.coffee)         # espresso
    # Try invalid order
    # bad_order = Order("not a customer", coffee, 5.0)  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# Property usage
# order.price = 7.5  # Valid
# try:
#     order.price = 15.0  # Raises ValueError
# except ValueError as e:
#     print(f"Error: {e}")
