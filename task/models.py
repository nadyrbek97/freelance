from django.db import models
from users.models import CustomUser


class Task(models.Model):
    NEW = 1
    IN_PROGRESS = 2
    ACCEPTED = 3
    NOT_ACCEPTED = 4
    STATUS = (
        (NEW, 'NEW'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (ACCEPTED, 'ACCEPTED'),
        (NOT_ACCEPTED, 'NOT_ACCEPTED')
    )
    title = models.CharField(max_length=400)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    executor = models.ForeignKey(CustomUser, related_name='executor', on_delete=models.CASCADE, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=NEW)

    def __str__(self):
        return self.title
