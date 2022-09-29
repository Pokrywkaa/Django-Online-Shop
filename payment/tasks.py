import weasyprint

from io import BytesIO
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from myshop.celery import app
from orders.models import Order

@app.task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = f'My Shop - EE Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent 4iu purchase.'
    email = EmailMessage(subject,
                        message,
                        to=[order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                                        stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf',
                out.getvalue(),
                'application/pdf')
    # send e-mail
    email.send()