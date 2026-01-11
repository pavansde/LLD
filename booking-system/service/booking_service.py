from factory.booking_factory import BookingFactory
from factory.payment_factory import PaymentFactory
from notification.observer import NotificationObserver


class BookingService:
    def __init__(self):
        self.observers: list[NotificationObserver] = []

    def register_observer(self, observer: NotificationObserver):
        self.observers.append(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.notify(message)

    def process_booking(
        self,
        booking_type: str,
        booking_data: dict,
        payment_type: str,
        payment_data: dict
    ):
        # Create booking using factory
        booking = BookingFactory.create_booking(
            booking_type=booking_type,
            **booking_data
        )

        # Booking flow
        booking.validate()
        amount = booking.calculate_total_price()
        booking.book()

        # Create payment using factory
        payment = PaymentFactory.create_payment(
            payment_type=payment_type,
            **payment_data
        )

        # Payment flow
        payment.pay(amount)

        # Notify observers
        self.notify(f"Amount; {amount} paid successfully")
