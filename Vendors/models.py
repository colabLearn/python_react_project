from django.db import models
from django_countries import countries
from django.core.validators import RegexValidator, EmailValidator


class VendorDisc(models.Model):
    
    COUNTRIES = list(countries)
    
    id = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=25)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    vendorID = models.CharField(max_length=50, unique=True, editable=False, blank=True)
    email = models.EmailField(
        validators=[EmailValidator(message='Enter a valid email address.')]
    )
    telephone = models.CharField(max_length=15)
    def save(self, *args, **kwargs):
        if self.id is None:
            super().save(*args, **kwargs)
        
        if self.id is not None:
            self.vendorID = "Bismo_{:05d}".format(self.id)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.vendorID + " " + self.companyName  
    class Meta:
        # Set the table name explicitly
        db_table = 'vendors'

# Create your models here.
