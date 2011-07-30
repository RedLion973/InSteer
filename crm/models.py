from django.db import models
from django.contrib.auth.models import User
from InSteer.settings import PHONE_NUMBER_TYPE_CHOICES

class Country(models.Model):
    name = models.CharField(max_length=500, unique=True)
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        verbose_name = u'Country'
        verbose_name_plural = u'Countries'

class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        verbose_name = u'Company'
        verbose_name_plural = u'Companies'

class Department(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    address = models.CharField(max_length=600)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=600)
    location = models.ForeignKey(Country)
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        verbose_name = u'Department'
        verbose_name_plural = u'Departments'

class Client(models.Model):
    department = models.ForeignKey(Department)
    user = models.ForeignKey(User)
    position = models.CharField(max_length=300)
    
    def human_readable_name(self):
        return self.user.get_full_name()
    human_readable_name.short_description = u'Complete Name'

    def __unicode__(self):
        return self.human_readable_name()
    
    class Meta:
        verbose_name = u'Client'
        verbose_name_plural = u'Clients'
    
class PhoneNumber(models.Model):
    client = models.ForeignKey(Client)
    type = models.CharField(max_length=50, choices=PHONE_NUMBER_TYPE_CHOICES)
    number = models.CharField(max_length=20)
    
    def __unicode__(self):
        return u'%s : %s' % (self.type, self.number)
    
    class Meta:
        verbose_name = u'Phone Number'
        verbose_name_plural = u'Phone Numbers'