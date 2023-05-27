import ipdb
from classes.customer import *
from classes.hotel import *
from classes.review import *

customer1 = Customer("James", "Smith")
customer2 = Customer("William", "Anderson")
customer3 = Customer("Ava", "Campbell")

hotel1 = Hotel("Marriott")
hotel2 = Hotel("Hampton Inn")
hotel3 = Hotel("Holiday Inn")

review1 = Review(customer1, hotel1, 5)
review2 = Review(customer1, hotel2, 5)
review3 = Review(customer2, hotel1, 4)
review4 = Review(customer1, hotel1, 3)

ipdb.set_trace()