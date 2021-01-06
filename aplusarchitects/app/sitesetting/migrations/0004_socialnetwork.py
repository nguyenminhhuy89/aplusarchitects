# Generated by Django 2.2.3 on 2019-07-18 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0003_sitesettings_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Social name')),
                ('icon', models.CharField(blank=True, max_length=100, verbose_name='Social icon')),
                ('link', models.CharField(max_length=255, verbose_name='Social link')),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitesetting.SiteSettings')),
            ],
        ),
    ]
