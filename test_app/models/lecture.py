from django.db import models
from django.contrib.auth.models import User

class LectureUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
