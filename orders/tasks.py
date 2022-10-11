import email
from django.core.mail import EmailMessage
from myshop.celery import app
from .models import Order

@app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'You have successfully placed and order.' \
              f'Your order ID is {order.id}.'
    email = EmailMessage(subject,
                            message,
                            to=[order.email])
    email.send()