# Generated by Django 2.2.4 on 2019-08-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='istuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
