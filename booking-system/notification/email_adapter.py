from notification.observer import NotificationObserver
from notification.third_party_email import ThirdPartyEmailService


class EmailNotificationAdapter(NotificationObserver):
    """
    Adapter that makes ThirdPartyEmailService compatible
    with NotificationObserver interface.
    """

    def __init__(self, email_service: ThirdPartyEmailService, to_address: str):
        self.email_service = email_service
        self.to_address = to_address

    def notify(self, message: str):
        self.email_service.send_mail(
            to_address=self.to_address,
            body=message
        )
