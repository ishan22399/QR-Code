# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Profile model to store user information
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default="N/A")
    phone_number = models.CharField(max_length=15)
    country_code = models.CharField(max_length=5, default="IN")  # Store country code
    dob = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# ActionLog model to track user actions (e.g., profile edits)
class ActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"
