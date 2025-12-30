from booking.booking import Booking

class MovieBooking(Booking):
    def __init__(self, movie_name: str, price: float, seats: int):
        self.movie_name = movie_name
        self.price = price
        self.seats = seats
        self.total_price = 0

    def validate(self):
        if self.seats < 0:
            raise ValueError("Seats cannot be negative")
        if self.price < 0:
            raise ValueError("Price cannot be negative")

    def calculate_total_price(self):
        self.total_price = self.price * self.seats
        return self.total_price

    def book(self):
        print(f"Booking for {self.movie_name} with {self.seats} seats at ${self.price} each.")
        print(f"Total price: ${self.total_price}")