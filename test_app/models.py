from django.db import models


class UserData(models.Model):
    name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    dob = models.DateField(blank=False, null=False)
    number = models.CharField(max_length=100, blank=True)
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_modification = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + " || " + self.email