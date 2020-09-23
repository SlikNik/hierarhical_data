from django.db import models
from django.contrib.auth.models import AbstractUser

class DataOwner(AbstractUser):
    BUSINESS = 1
    PERSONAL = 2
    TEACHER = 3
    STUDENT = 4
    ACCOUNT_CHOICES = (
        ('', ('Choose your account type')),
        (str(BUSINESS), ('1 - Business')),
        (str(PERSONAL), ('2 - Personal')),
        (str(TEACHER), ('3 - Teacher')),
        (str(STUDENT), ('4 - Student'))
    )
    display_name = models.CharField(max_length=120, blank=True, null=True)
    account_type = models.CharField(choices=ACCOUNT_CHOICES, max_length=1, blank=True, null=True)
    REQUIRED_FIELDS = ['display_name', 'first_name', 'last_name', 'email']
    
    def __str__(self):
        return self.username

