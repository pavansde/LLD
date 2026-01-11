from notification.observer import NotificationObserver

class EmailNotifier(NotificationObserver):
    def notify(self, message:str):
        print(f"Email: {message}")