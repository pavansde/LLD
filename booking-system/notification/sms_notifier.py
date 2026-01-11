from notification.observer import NotificationObserver

class SMSNotifier(NotificationObserver):
    def notify(self, message:str):
        print(f"SMS: {message}")