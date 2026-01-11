from payment.payment_decorator import PaymentDecorator


class RetryPaymentDecorator(PaymentDecorator):

    def __init__(self, wrapped, retries: int = 3):
        super().__init__(wrapped)
        self.retries = retries

    def pay(self, amount: float):
        for attempt in range(1, self.retries + 1):
            try:
                print(f"[RETRY] Attempt {attempt}")
                return self._wrapped.pay(amount)
            except Exception as e:
                print(f"[RETRY] Failed attempt {attempt}: {e}")
                if attempt == self.retries:
                    raise
