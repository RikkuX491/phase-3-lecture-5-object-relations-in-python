from classes.review import Review

class Customer:

    all = []
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.all.append(self)

    def reviews(self):
        return [review for review in Review.all if review.customer is self]
    
    def hotels(self):
        return list(set([review.hotel for review in Review.all if review.customer is self]))