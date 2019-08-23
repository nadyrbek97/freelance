from django.contrib.auth.models import AbstractUser
from django.db import models, transaction


class CustomUser(AbstractUser):
    CUSTOMER = 1
    EXECUTOR = 2
    ROLE = (
        (CUSTOMER, 'CUSTOMER'),
        (EXECUTOR, 'EXECUTOR')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE, default=CUSTOMER)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    @classmethod
    def withdraw(cls, customer_id, price):
        with transaction.atomic():
            customer = (cls.objects.select_for_update().get(id=customer_id))
            customer.balance = models.F('balance') - price
            customer.save()
        return customer

    @classmethod
    def get_payment(cls, user_id, price):
        with transaction.atomic():
            user = (cls.objects.select_for_update().get(id=user_id))
            user.balance = models.F('balance') + price
            user.save()
        return user




