from django.db import models

class User(models.Model):
    name = models.CharField(max_length=15)
    pas = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return self.name
