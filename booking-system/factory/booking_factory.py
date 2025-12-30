from booking.movie_booking import MovieBooking
from booking.booking import Booking


class BookingFactory:

    @staticmethod
    def create_booking(booking_type: str, **kwargs) -> Booking:
        if booking_type == "movie":
            return MovieBooking(
                movie_name=kwargs["movie_name"],
                price=kwargs["price"],
                seats=kwargs["seats"]
            )

        raise ValueError(f"Unsupported booking type: {booking_type}")
