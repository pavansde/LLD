from payment.upi_payment import UPIPayment


def test_upi_payment_executes_without_error():
    payment = UPIPayment("test@upi")
    payment.pay(100)  # should not raise
