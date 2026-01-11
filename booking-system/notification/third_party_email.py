class ThirdPartyEmailService:
    """
    Simulates an external email SDK.
    Note the interface does NOT match our observer.
    """

    def send_mail(self, to_address: str, body: str):
        print(f"[3RD PARTY EMAIL] To: {to_address} | Message: {body}")
