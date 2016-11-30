# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 14:22
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('pseudo', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('firstName', models.CharField(blank=True, max_length=100, null=True)),
                ('lastName', models.CharField(blank=True, max_length=100, null=True)),
                ('facebookId', models.CharField(blank=True, max_length=100, null=True)),
                ('pushToken', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='media')),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('online', models.BooleanField(default=0)),
                ('lastConnexionDate', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('valide', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('zipCode', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('mainPhoto', models.ImageField(blank=True, null=True, upload_to='media')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('valide', models.BooleanField(default=1)),
                ('refCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='media')),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('valide', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('valide', models.BooleanField(default=1)),
                ('refLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.Lieu')),
                ('refPhoto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.Photo')),
            ],
        ),
        migrations.AddField(
            model_name='favori',
            name='refLieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.Lieu'),
        ),
        migrations.AddField(
            model_name='favori',
            name='refUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.AppUser'),
        ),
    ]