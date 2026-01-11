from payment.payment import Payment


class PaymentDecorator(Payment):
    """
    Base decorator that wraps a PaymentStrategy.
    """

    def __init__(self, wrapped: Payment):
        self._wrapped = wrapped

    def pay(self, amount: float):
        return self._wrapped.pay(amount)
