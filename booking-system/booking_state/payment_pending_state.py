from booking_state.state import BookingState
from booking_state.paid_state import PaidState


class PaymentPendingState(BookingState):

    def pay(self, context):
        print("Payment successful.")
        context.set_state(PaidState())

    def cancel(self, context):
        print("Booking cancelled during payment.")
        context.set_state(None)
