# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

import datetime


class DemoInfo(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    host = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=20)
    source = models.CharField(max_length=50)
    source_latitude = models.FloatField()
    source_longitude = models.FloatField()
    destination = models.CharField(max_length=50, blank=True, null=True)
    destination_latitude = models.FloatField(blank=True, null=True)
    destination_longitude = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=5)
    sdate = models.DateTimeField()
    edate = models.DateTimeField(blank=True, null=True)
    cdate = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'demo_info'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
