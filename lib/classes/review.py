class Review:

    all = []
    
    def __init__(self, customer, hotel, rating):
        self.customer = customer
        self.hotel = hotel
        self.rating = rating
        Review.all.append(self)