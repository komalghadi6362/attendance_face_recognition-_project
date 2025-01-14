# Generated by Django 4.0.4 on 2022-06-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('pk_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('pk_name', models.CharField(max_length=100)),
                ('pk_price', models.CharField(max_length=100)),
                ('pk_status', models.IntegerField(default=0, max_length=100)),
                ('pk_created_by', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
