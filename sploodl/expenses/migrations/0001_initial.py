# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Sploodl',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('home_currency', models.CharField(choices=[('GBP', 'British Pound Sterling'), ('USD', 'United States Dollar'), ('EUR', 'Euro'), ('DKK', 'Danish Krone'), ('SEK', 'Swedish Krona')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=140)),
                ('currency', models.CharField(choices=[('GBP', 'British Pound Sterling'), ('USD', 'United States Dollar'), ('EUR', 'Euro'), ('DKK', 'Danish Krone'), ('SEK', 'Swedish Krona')], max_length=3)),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('people_by', models.ManyToManyField(related_name='_transaction_people_by_+', to='expenses.Participant')),
                ('people_for', models.ManyToManyField(related_name='_transaction_people_for_+', to='expenses.Participant')),
                ('sploodl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.Sploodl')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='sploodl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.Sploodl'),
        ),
    ]
