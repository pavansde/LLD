import pytest
from booking.movie_booking import MovieBooking


def test_movie_booking_price_calculation():
    booking = MovieBooking("Interstellar", price=100, seats=2)
    assert booking.calculate_total_price() == 200


def test_movie_booking_invalid_seats():
    booking = MovieBooking("Interstellar", price=100, seats=0)
    with pytest.raises(ValueError):
        booking.validate()
