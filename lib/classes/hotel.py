from classes.review import Review

class Hotel:

    all = []
    
    def __init__(self, name):
        self.name = name
        Hotel.all.append(self)

    def reviews(self):
        return [review for review in Review.all if review.hotel is self]
    
    def customers(self):
        return list(set([review.customer for review in Review.all if review.hotel is self]))