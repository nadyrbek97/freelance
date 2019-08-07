from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    CUSTOMER = 1
    EXECUTOR = 2
    ROLE = (
        (CUSTOMER, 'CUSTOMER'),
        (EXECUTOR, 'EXECUTOR')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE, default=CUSTOMER)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
