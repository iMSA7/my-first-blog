# Generated by Django 3.0.8 on 2020-07-12 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200706_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='education',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='cv',
            name='interests',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='cv',
            name='referees',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='cv',
            name='voluntary',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='cv',
            name='work',
            field=models.TextField(default='None'),
        ),
    ]