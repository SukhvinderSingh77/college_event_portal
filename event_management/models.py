# python
from django.db import models
from django.contrib.auth.models import User
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Pending')
    name = models.CharField(max_length=255)  # added
    email = models.EmailField()  # added
    phone = models.CharField(max_length=20)  # added

    def __str__(self):
        return f'{self.user.username} - {self.event.name}'