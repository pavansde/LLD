from abc import ABC, abstractmethod


class BookingState(ABC):
    """
    Defines actions allowed in a booking state.
    """

    @abstractmethod
    def pay(self, context):
        pass

    @abstractmethod
    def cancel(self, context):
        pass
