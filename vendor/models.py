from django.db import models
import uuid
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)


class PurchaseOrder(models.Model):
    ORDER_PENDING = 'pending'
    ORDER_COMPLETED = 'completed'
    ORDER_CANCELED = 'canceled'

    ORDER_CHOICES = [
        (ORDER_PENDING, 'pending'),
        (ORDER_COMPLETED, 'completed'),
        (ORDER_CANCELED, 'canceled'),
    ]

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=9, choices=ORDER_CHOICES, default=ORDER_PENDING)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()    
    