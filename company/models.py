from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=45)
    desc = models.CharField(max_length=45)
    website = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    logo = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'company'