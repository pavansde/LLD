from payment.upi_payment import UPIPayment
from payment.card_payment import CardPayment
from payment.payment import Payment


class PaymentFactory:

    @staticmethod
    def create_payment(payment_type: str, **kwargs) -> Payment:
        if payment_type == "upi":
            return UPIPayment(upi_id=kwargs["upi_id"])

        if payment_type == "card":
            return CardPayment(card_number=kwargs["card_number"])

        raise ValueError(f"Unsupported payment type: {payment_type}")
