from django.db import models

class Names(models.Model):
    first = models.CharField(max_length=35)
    last = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.first} {self.last}")

    def __repr__(self):
        return (f"id: {self.id} :{self.first} {self.last}")