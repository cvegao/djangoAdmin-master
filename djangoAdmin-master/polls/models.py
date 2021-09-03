from django.db import models


class Client(models.Model):
    id = models.AutoField(db_column='client_id', primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    joined_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clients'


class Site(models.Model):
    id = models.AutoField(db_column='site_id', primary_key=True)
    domain_name = models.CharField(max_length=100)
    created_datetime = models.DateTimeField()
    client=models.ForeignKey(Client, related_name="sites",on_delete=models.CASCADE)#client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sites'


class Lead(models.Model):
    id = models.AutoField(db_column='lead_id',primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registered_datetime = models.DateTimeField()
    email = models.CharField(max_length=50)
    site=models.ForeignKey(Site, related_name="leads", on_delete=models.CASCADE)#site_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leads'


class Documento(models.Model):
    id = models.AutoField(db_column='billing_id',primary_key=True)
    amount = models.FloatField()
    charged_datetime = models.DateTimeField()
    client=models.ForeignKey(Client, related_name="billing",on_delete=models.CASCADE)#client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'billing'