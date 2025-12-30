from service.booking_service import BookingService


if __name__ == "__main__":
    service = BookingService()

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
