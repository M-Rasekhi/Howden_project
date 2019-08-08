from django.db import models
import datetime
from django import forms

# Create your models here.


class Rectangle(models.Model):
    rec_width = models.DecimalField(max_digits=10, decimal_places=2)
    rec_height = models.DecimalField(max_digits=10, decimal_places=2)
    date_recorded = models.DateField(auto_now=True)


class FanUnbalance(models.Model):
    BALANCE_CHOICE = ['1', '2.5', '6.3']
    balance_grade = models.CharField(max_length=10, choices=[(x, x) for x in BALANCE_CHOICE], default='2.5')
    impeller_mass = models.DecimalField(max_digits=10, decimal_places=2)
    fan_speed = models.DecimalField(max_digits=10, decimal_places=2)
    backplate_dia = models.DecimalField(max_digits=10, decimal_places=2)

class EarthQuake(models.Model):
    SITECLASS_CHOICES = ['A', 'B', 'C', 'D', 'E']
    RISK_CHOICES = ['1', '2', '3', '4']
    STRUCT_TYPE_CHOICES = ("Steel moment-resisting frames", "Concrete moment-resisting frames", "Steel eccentrically braced frames in accordance with Table 12.2-1 lines B1 or D1", "Steel buckling-restrained braced frames", "All other structural systems")
    site_class = models.CharField(max_length=1, choices=[(x, x) for x in SITECLASS_CHOICES], default='D')
    res_mod_coeff= models.DecimalField('R Value', max_digits=6, decimal_places=5, default=3)
    risk_cat = models.CharField('Risk Category', max_length=100, choices=[(x, x) for x in RISK_CHOICES], default='2')
    s1= models.DecimalField('S1', max_digits=6, decimal_places=5)
    ss= models.DecimalField('Ss', max_digits=6, decimal_places=5)
    fund_period = models.DecimalField('T', max_digits=6, decimal_places=3)
    long_period = models.DecimalField('TL', max_digits=6, decimal_places=3)
    height = models.DecimalField('Height', max_digits=6, decimal_places=3)
    structure_type = models.CharField('Structure Type', max_length=100, choices=[(x, x) for x in STRUCT_TYPE_CHOICES], default= "All other structural systems")
    site_class_calculated = models.BooleanField(default=False)

