# Generated by Django 2.2.3 on 2019-07-10 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'permissions': (('manage_sitesettings', 'Manage site settings.'),)},
        ),
    ]
