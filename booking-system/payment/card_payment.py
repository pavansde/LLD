from payment.payment import Payment

class CardPayment(Payment):
    def __init__(self, total_price: float):
        self.total_price = total_price

    def pay(self):
        print(f"Paying ${self.total_price}")
        print("Payment successful")