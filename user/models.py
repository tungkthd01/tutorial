
from  django.db import models

class clients(models.Model):
    client_id = models.IntegerField(null=False,primary_key=True)
    name = models.CharField(null=False,max_length=255)
    seconds_delivered_per_month = models.DecimalField(null = False,max_digits=15, decimal_places=0)
    is_archived = models.SmallIntegerField(null = False, choices=[(0,'Not archived'),(1,'Archived')])
    created_at = models.DateTimeField(null = False,auto_now_add=True)
    updated_at = models.DateTimeField(null = False,auto_now=True)
    class Meta:
        db_table = 'clients'

class users(models.Model):
    user_id = models.IntegerField(null = False, primary_key=True)
    client_id = models.IntegerField(null=False)
    user_type = models.SmallIntegerField(null=False, choices=[(1,'General user'),(2,'Host user')])
    login_type = models.CharField(null=False,max_length=45, choices=[(1, 'EMAIL'),(2, 'INSTAGRAM'),(3, 'FACEBOOK'),(4, 'TWITTER')])
    created_at = models.DateTimeField(null=False,auto_now_add=True)
    updated_at = models.DateTimeField(null=False,auto_now=True)
    class Meta:
        db_table ='users'