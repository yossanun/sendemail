from django.db import models
from django.db.models.fields import EmailField
class Email(models.Model):
    Emailname =  models.EmailField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.Emailname