# Generated by Django 4.0.2 on 2022-02-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_evento_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
