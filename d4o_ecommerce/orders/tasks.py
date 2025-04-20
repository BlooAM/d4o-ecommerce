from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order no. {order_id}'
    message = f'Hello {order.first_name}, \n\n' \
              'You have created order in our shop. ' \
              f'Identifier of the order: {order.id}'

    mail_sent = send_mail(subject, message, 'admin@mail.com', [order.email])
    return mail_sent
