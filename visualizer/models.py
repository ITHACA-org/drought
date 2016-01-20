from django.db import models

class SSIAfr(models.Model):
    fid = models.IntegerField(primary_key=True)
    # the_geom = models.TextField(blank=True) # This field type is a guess.
    # location = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    # category = models.CharField(max_length=255, blank=True)
    # unixtime = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ssi_afr'

class SPI3Month(models.Model):
    fid = models.IntegerField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'spi_3month'
