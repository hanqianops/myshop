from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def add(x,y):
    return x+y

@task
def order_created(order_id):
    """
    订单创建成功后发送邮件
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name,
                                            order.id)
    mail_sent = send_mail(subject,
                        message,
                        'admin@myshop.com',
                        [order.email])
    return mail_sent