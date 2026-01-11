from booking_state.state import BookingState
from booking_state.payment_pending_state import PaymentPendingState


class CreatedState(BookingState):

    def pay(self, context):
        print("Payment initiated.")
        context.set_state(PaymentPendingState())

    def cancel(self, context):
        print("Booking cancelled from CREATED state.")
        context.set_state(None)
