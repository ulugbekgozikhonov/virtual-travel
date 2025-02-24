from django.db import models
from users.models import User, Base
import uuid

class TravelAgency(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agencies")
    contact_info = models.TextField()
    description = models.TextField()
    logo = models.ImageField(upload_to="agency_logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    flag = models.ImageField(upload_to="flags/", blank=True, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="cities/", blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.country.name}"

