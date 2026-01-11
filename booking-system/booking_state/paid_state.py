from booking_state.state import BookingState
from booking_state.confirmed_state import ConfirmedState


class PaidState(BookingState):

    def pay(self, context):
        print("Already paid.")

    def cancel(self, context):
        print("Cannot cancel after payment.")
