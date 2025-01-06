from django.core.mail import EmailMultiAlternatives


def send_email(user,subject,body): 
        email = EmailMultiAlternatives(
            subject=subject,
            body='',
            from_email= 'LibZone -anmamun0 | <noreply@example.com>',
            to=[user.email],
        )
        email.attach_alternative(body, "text/html")
        email.send()