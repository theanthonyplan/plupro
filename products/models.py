from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
#model for proposal line item objects
class Product(models.Model):
    UM_CHOICES = [
        ('EA', 'EA'),
        ('FT', 'FT'),
    ]

    # model field for the customer's name, should never be blank, max length of 60
    name = models.CharField(unique=True, blank=False, max_length=60)
    description = models.TextField(blank=True, max_length=9000)
    price = models.FloatField(blank=False, default=1.0)
    um = models.CharField(blank=False, choices=UM_CHOICES, default='EA', max_length=2)
    tags = TaggableManager()
    # category = models.ForeignKey(ProposalLineCategory, blank=False, null=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Products"
    def __str__(self):
            return self.name
    # this is how an object will represent itself (as a string)
    def __repr__(self):
            return str("Product: " + self.name)
