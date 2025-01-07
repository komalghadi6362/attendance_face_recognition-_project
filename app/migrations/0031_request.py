# Generated by Django 4.0.5 on 2022-08-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_remove_category_ct_request_hall_h_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('rq_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('rq_name', models.CharField(default='', max_length=100)),
                ('rq_email', models.CharField(default='', max_length=100)),
                ('rq_mobile', models.CharField(default='', max_length=100)),
                ('rq_status', models.CharField(default='0', max_length=100)),
                ('rq_created_by', models.CharField(max_length=100)),
            ],
        ),
    ]