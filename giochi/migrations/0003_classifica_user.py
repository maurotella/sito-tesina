# Generated by Django 2.0.5 on 2018-06-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giochi', '0002_classifica_gioco'),
    ]

    operations = [
        migrations.AddField(
            model_name='classifica',
            name='user',
            field=models.CharField(default='anonimo', max_length=30),
        ),
    ]
