from django.db import models
from django.conf import settings
from properties.models import Listing, Booking

# TODO: Another Member to implement logic for the following entities:

class PriceAdjustment(models.Model):
    # Connected to Listing
    pass

class HostPayout(models.Model):
    # Connected to Booking & Host
    pass

class Payment(models.Model):
    # Connected to Booking
    pass

class AdminLog(models.Model):
    # Standalone logging entity
    pass
