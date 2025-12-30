# validate the input
# calculate the total price
# book

from abc import ABC, abstractmethod

class Booking(ABC):
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def calculate_total_price(self) -> float:
        pass
    
    @abstractmethod
    def book(self):
        pass