from django.contrib.auth.models import Group, User
from django.db import models
from django.shortcuts import reverse

from organizations.models import Position
from recruitment.models import Company


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    interested_in = models.TextField(choices=Position.Department.choices)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user} profile"

    def get_absolute_url(self):
        return reverse("company-admin")
