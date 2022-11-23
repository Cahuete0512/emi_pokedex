# Generated by Django 4.1.3 on 2022-11-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciesName', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('picture', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=30)),
                ('abilities', models.CharField(max_length=30)),
                ('catchRate', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=30)),
                ('weight', models.CharField(max_length=30)),
            ],
        ),
    ]