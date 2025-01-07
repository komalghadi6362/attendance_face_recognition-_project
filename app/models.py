from django.db import models
from django.utils import timezone

# Create your models here.


class AdminMaster(models.Model):
    ad_id = models.AutoField(primary_key=True, unique=True)
    ad_name = models.CharField(max_length=100)
    ad_mobile = models.CharField(max_length=100)
    ad_email = models.CharField(max_length=100)
    ad_password = models.CharField(max_length=100)
    ad_role = models.CharField(max_length=100)
    ad_status = models.IntegerField(default=0)
    ad_created_by = models.CharField(max_length=100)


class Class(models.Model):
    cl_id = models.AutoField(primary_key=True, unique=True)
    cl_day_id = models.CharField(max_length=100)
    cl_time = models.CharField(max_length=100, default="")
    cl_faculty_id = models.CharField(max_length=100, default="")
    cl_subject_id = models.CharField(max_length=100, default="")
    cl_status = models.IntegerField(default=0)
    cl_created_by = models.CharField(max_length=100)


class Faculty(models.Model):
    fc_id = models.AutoField(primary_key=True, unique=True)
    fc_name = models.CharField(max_length=100)
    fc_mobile = models.CharField(max_length=100)
    fc_email = models.CharField(max_length=100)
    fc_role = models.CharField(max_length=100)
    fc_status = models.IntegerField(default=0)
    fc_created_by = models.CharField(max_length=100)


class Students(models.Model):
    us_id = models.AutoField(primary_key=True, unique=True)
    us_name = models.CharField(max_length=100, default="")
    us_email = models.CharField(max_length=100)
    us_parent_email = models.CharField(max_length=100)
    us_mobile = models.CharField(max_length=100, default="")
    us_usn = models.CharField(max_length=100, default="")
    us_address = models.CharField(max_length=100, default="")
    us_status = models.IntegerField(default=0)
    us_created_by = models.CharField(max_length=100, default="")


class Subject(models.Model):
    su_id = models.AutoField(primary_key=True, unique=True)
    su_name = models.CharField(max_length=100, default="")
    su_status = models.IntegerField(default=0)
    su_created_by = models.CharField(max_length=100, default="")


class Day(models.Model):
    day_id = models.AutoField(primary_key=True, unique=True)
    day_name = models.CharField(max_length=100, default="")
    day_status = models.IntegerField(default=0)
    day_created_by = models.CharField(max_length=100, default="")


class Attendance(models.Model):
    at_id = models.AutoField(primary_key=True, unique=True)
    at_student_id = models.CharField(max_length=100, default="")
    at_class_id = models.CharField(max_length=100)
    at_status = models.IntegerField(default=0)
    at_created_by = models.CharField(max_length=100, default="")
    at_date_time = models.DateTimeField(default=timezone.now)
