from service.booking_service import BookingService
# from notification.email_notifier import EmailNotifier
from notification.sms_notifier import SMSNotifier
from notification.email_adapter import EmailNotificationAdapter
from notification.third_party_email import ThirdPartyEmailService


if __name__ == "__main__":
    service = BookingService()
    # service.register_observer(EmailNotifier())
    email_service = ThirdPartyEmailService()
    email_adapter = EmailNotificationAdapter(
        email_service=email_service,
        to_address="user@example.com"
    )
    service.register_observer(email_adapter)
    service.register_observer(SMSNotifier())

    service.process_booking(
        booking_type="movie",
        booking_data={
            "movie_name": "Interstellar",
            "price": 100,
            "seats": 2
        },
        payment_type="upi",
        payment_data={
            "upi_id": "dummy@upi"
        }
    )
