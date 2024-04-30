from django.db import models

# Create your models here.
class Client_Data(models.Model):

    CATEGORIES = (
        ('Corporate', 'Corporate/Company'),
        ('Individual', 'Individual'),
        ('School', 'School'),
        ('Government', 'Government'),
    )
    ENTITYTYPE = (
        ('Big Entity', 'Big Entity'),
        ('Small Entity', 'Small Entity')
    )
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Dormant', 'Dormant'),
        ('Delinquent', ' Delinquent')
    )

    client_number = models.CharField(max_length=30, blank=True, null=True)
    entity_type = models.CharField(max_length=20, choices=ENTITYTYPE, null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, null=True, blank=True)
    client_name = models.CharField(max_length=200)
    unit_description = models.CharField(max_length=50, blank=True, null=True)    
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country_name = models.CharField(max_length=30, blank=True, null=True)
    fax_number = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    website = models.CharField(max_length=60, null=True, blank=True )
    zip_code = models.CharField(max_length=30, blank=True)
    landline= models.CharField(max_length=100, blank=True)
    date_acquired = models.DateField(null=True, blank=True)
    date_entered = models.DateField(null=True, blank=True)
    client_type = models.CharField(max_length=1, blank=True, null=True) 
    account_officer = models.CharField(max_length = 50, blank=True, null=True) 
    account_person = models.CharField(max_length = 50, blank=True, null=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default="Active")
    remarks = models.TextField(blank=True, null=True)
    entered_by = models.CharField(max_length=15, blank=True, null=True)
    referredby = models.CharField(max_length=150, blank=True)
    billing_to = models.CharField(max_length=100, blank=True)
    billing_address = models.CharField(max_length=200, blank=True)
    billing_attention = models.CharField(max_length=60, blank=True)
    position = models.CharField(max_length=60, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updatedby = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'{self.client_name}'
