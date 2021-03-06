# Generated by Django 2.2.3 on 2019-08-02 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'permissions': (('manage_category', 'Manage portfolio categories.'),),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.Category')),
            ],
            options={
                'permissions': (('manage_category', 'Manage portfolio projects.'),),
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/projects/')),
                ('sort_order', models.IntegerField(default=0)),
                ('alt', models.CharField(blank=True, max_length=128)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.Project')),
            ],
            options={
                'ordering': ('sort_order',),
            },
        ),
        migrations.CreateModel(
            name='ProjectTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(choices=[('vi', 'Vietnamese'), ('en', 'English')], max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(verbose_name='Description')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='portfolio.Project')),
            ],
            options={
                'unique_together': {('language_code', 'project')},
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(choices=[('vi', 'Vietnamese'), ('en', 'English')], max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='portfolio.Category')),
            ],
            options={
                'unique_together': {('language_code', 'category')},
            },
        ),
    ]
