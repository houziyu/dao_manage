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
    def __str__(self):
        return self.name

class all_parameter(models.Model):
    parameter = models.CharField(max_length=20)
    def __str__(self):
        return self.parameter


class script_data(models.Model):
    script_name = models.CharField(max_length=40)
    script_path = models.CharField(max_length=100)
    service_name = models.CharField(max_length=40)
    server_name = models.CharField(max_length=40)
    script_parameter = models.ManyToManyField(all_parameter,blank=True)
    def __str__(self):
        return self.script_name