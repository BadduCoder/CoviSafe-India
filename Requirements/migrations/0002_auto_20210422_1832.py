# Generated by Django 3.2 on 2021-04-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requirements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='primary_contact',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='secondary_contact',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
