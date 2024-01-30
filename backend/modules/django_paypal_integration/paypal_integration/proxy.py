import paypalrestsdk
from paypalrestsdk.orders import Order
from django.conf import settings


class PayPalProxy:
    def __init__(self):
        paypalrestsdk.configure({
            "mode": settings.PAYPAL_MODE,  # sandbox or live
            "client_id": settings.PAYPAL_CLIENT_ID,
            "client_secret": settings.PAYPAL_CLIENT_SECRET
        })

    def create_order(self, order_data):
        order = Order({'intent': 'CAPTURE', **order_data})
        if order.create():
            return order
        else:
            return None

    def capture_order(self, order_id):
        order = Order.find(order_id)
        return order.capture() if order else None

    def authorize_order(self, order_id):
        order = Order.find(order_id)
        return order.authorize() if order else None

    def show_order(self, order_id):
        return Order.find(order_id)

    def list_orders(self):
        return Order.all()