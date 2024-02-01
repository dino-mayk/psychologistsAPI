from django.db import models


class BaseContact(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.type})"


class PhoneNumber(BaseContact):
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.phone_number} ({self.type})"


class Address(BaseContact):
    address = models.TextField()

    def __str__(self):
        return f"{self.address} ({self.type})"


class Email(BaseContact):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} ({self.type})"
