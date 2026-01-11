from service.booking_service import BookingService


class DummyObserver:
    def __init__(self):
        self.messages = []

    def notify(self, message: str):
        self.messages.append(message)


def test_booking_service_triggers_notification():
    service = BookingService()
    observer = DummyObserver()
    service.register_observer(observer)

    service.process_booking(
        booking_type="movie",
        booking_data={
            "movie_name": "Interstellar",
            "price": 100,
            "seats": 2
        },
        payment_type="upi",
        payment_data={
            "upi_id": "test@upi"
        }
    )

    assert "paid" in observer.messages[0].lower()
    assert "200" in observer.messages[0]

