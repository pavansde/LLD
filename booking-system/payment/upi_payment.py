from payment.payment import Payment


class UPIPayment(Payment):

    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float):
        print(f"Processing UPI payment of ${amount} for {self.upi_id}")
        print("UPI payment successful")
