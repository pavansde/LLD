from booking_state.state import BookingState


class ConfirmedState(BookingState):

    def pay(self, context):
        print("Already confirmed.")

    def cancel(self, context):
        print("Cannot cancel confirmed booking.")
