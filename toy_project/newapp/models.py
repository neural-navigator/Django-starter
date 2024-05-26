from django.db import models
from django.utils import timezone

# Create your models here.
class NewVariety(models.Model):
    COLOR = [
        ('1', 'Blue'),
        ('2', 'Yellow'),
        ('3', 'Red')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static_uploads/')
    created_on = models.DateField(default=timezone.now)
    type = models.CharField(max_length=1, choices=COLOR)
