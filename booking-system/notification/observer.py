from abc import ABC, abstractmethod

class NotificationObserver(ABC):
    @abstractmethod
    def notify(self, message:str):
        pass