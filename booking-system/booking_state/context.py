from booking_state.created_state import CreatedState


class BookingContext:
    """
    Maintains current booking state and delegates behavior to it.
    """

    def __init__(self):
        self._state = CreatedState()

    def set_state(self, state):
        self._state = state

    def pay(self):
        if self._state:
            self._state.pay(self)
        else:
            print("No active booking.")

    def cancel(self):
        if self._state:
            self._state.cancel(self)
        else:
            print("No active booking.")
            
if __name__ == "__main__":
    booking = BookingContext()

    booking.pay()      # CREATED → PAYMENT_PENDING
    booking.pay()      # PAYMENT_PENDING → PAID
    booking.cancel()   # Cannot cancel after payment
