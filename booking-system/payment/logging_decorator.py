from payment.payment_decorator import PaymentDecorator


class LoggingPaymentDecorator(PaymentDecorator):

    def pay(self, amount: float):
        print(f"[LOG] Starting payment of ${amount}")
        result = self._wrapped.pay(amount)
        print(f"[LOG] Payment of ${amount} completed")
        return result
