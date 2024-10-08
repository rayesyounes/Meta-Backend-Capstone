from ..models import Booking, Menu
from random import randint
import requests

BOOKINGS = {
    1: {'name': 'Vill'},
    2: {'name': 'Jani', 'no_og_guests': randint(1, 11)},
    3: {'name': 'Niilo', 'no_og_guests': randint(1, 11)},
    4: {'name': 'Markus', 'no_og_guests': randint(1, 11)},
}

MENU_ITEMS = {
    1: {'title': 'ApplePie', 'price': 13.78},
    2: {'title': 'Latte', 'price': 3.99, 'inventory': randint(0, 11)},
    3: {'title': 'Icecream', 'price': 5.00, 'inventory': randint(0, 11)},
    4: {'title': 'IrishCoffe', 'price': 7.89, 'inventory': randint(0, 11)},
}


class CreateBookingsMixin:
    bookings = BOOKINGS

    def create_bookings(self):
        for idx in self.bookings.keys():
            booking = Booking.objects.create(
                name=self.bookings[idx]['name'],
            )
            if self.bookings[idx].get('no_of_guests') is not None:
                booking.no_of_guests = self.bookings[idx]['no_of_guests'],
            if self.bookings[idx].get('booking_date') is not None:
                print(self.bookings[idx]['booking_date'])
                booking.booking_date = self.bookings[idx]['booking_date'],
            booking.save()


class CreateMenuItemsMixin:
    items = MENU_ITEMS

    def create_menu_items(self):
        for idx in self.items.keys():
            item = Menu.objects.create(
                title=self.items[idx]['title'],
                price=self.items[idx]['price'],
            )
            if self.items[idx].get('inventory') is not None:
                item.inventory = self.items[idx].get('inventory')
            item.save()


class UserMixin:

    def create_user(self, username, password):
        url = 'http://127.0.0.1:8000/auth/users/'
        data = {
            'username': username,
            'password': password,
        }
        return requests.post(url, data=data)

    def get_token(self, username, password):
        url = 'http://127.0.0.1:8000/api/token/login/'
        data = {
            'username': username,
            'password': password,
        }
        return requests.post(url, data=data).json().get('access')

    def get_auth_header(self, token):
        return {'Authorization': f'JWT {token}'}
