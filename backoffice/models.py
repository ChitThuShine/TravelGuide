from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from backoffice.signals import *
from django.db.models.signals import *

# Models here.
class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __unicode__(self):
       return u'%s' % (self.name)

class Photo(models.Model):
    picture = models.ImageField(upload_to="media", null=True, blank=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    valide = models.BooleanField(default=1)

    def __unicode__(self):
       return u'%s' % (self.picture)

class Lieu(models.Model):
    name = models.CharField(max_length=100)
    refCategory = models.ForeignKey(Category)
    street = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mainPhoto = models.ImageField(upload_to="media", default='media/avatarlieux.jpg',null=True, blank=True)
    photos = models.ManyToManyField(Photo, through='PhotoLieu')
    location = models.PointField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    valide = models.BooleanField(default=1)

    def __unicode__(self):
       return u'%s - %s' % (self.name,self.refCategory)

class PhotoLieu(models.Model):
    refLieu = models.ForeignKey(Lieu)
    refPhoto = models.ForeignKey(Photo)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    valide = models.BooleanField(default=1)

    def __unicode__(self):
       return u'%s - %s' % (self.refLieu,self.refPhoto)

class AppUser(models.Model):
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    pseudo = models.CharField(max_length=100, null=True, blank=True,unique=True)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    facebookId = models.CharField(max_length=100, null=True, blank=True)
    pushToken = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to="media",default='media/avatar.jpg', null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    location  = models.PointField(null=True, blank=True)
    online = models.BooleanField(default=0)
    lastConnexionDate = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    valide = models.BooleanField(default=1)
    favoris = models.ManyToManyField(Lieu, through='Favori')

    def __unicode__(self):
       return u'%s' % (self.email)

post_save.connect(signal_add_user, dispatch_uid="signal_add_user",sender=AppUser)
post_delete.connect(signal_delete_model, sender=AppUser, dispatch_uid="delete_user")


class Favori(models.Model):
    refLieu = models.ForeignKey(Lieu)
    refUser = models.ForeignKey(AppUser)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)


class AppUserStats(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    month = models.DateField()
    nbFavoris = models.IntegerField()
    nbPhotos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'backoffice_userstatistiques'