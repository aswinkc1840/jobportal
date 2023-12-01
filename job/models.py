from django.db import models
from company.models import Company
# from job.models import Job
# Create your models here.

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=45)
    desc = models.CharField(max_length=45)
    post_date = models.DateTimeField()
    location = models.CharField(max_length=45)
    vacancy = models.IntegerField(blank=True, null=True)
    job_nature = models.CharField(max_length=45)
    salary = models.CharField(max_length=45)
    appli_date = models.DateTimeField()
    skills = models.CharField(max_length=300)
    education = models.CharField(max_length=300)
    experience = models.IntegerField()
    # company_id = models.IntegerField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'job'


class AppliedJob(models.Model):
    apply_id = models.AutoField(primary_key=True)
    # job_id = models.IntegerField(blank=True, null=True)
    # company_id = models.CharField(max_length=45)
    resume = models.CharField(max_length=300)
    user_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    appied_date = models.DateTimeField()
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'applied_job'