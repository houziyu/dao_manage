from django.db import models

class monitoring_data(models.Model):
    cpu = models.FloatField()
    mem_usage = models.FloatField()
    mem = models.FloatField()
    net_i = models.FloatField()
    net_o = models.FloatField()
    datetime = models.DateTimeField(auto_now = True)
    container_name = models.CharField(max_length=30,default=None)
    name = models.CharField(max_length=30)
