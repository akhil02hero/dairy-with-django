# Generated by Django 3.0.5 on 2020-04-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
