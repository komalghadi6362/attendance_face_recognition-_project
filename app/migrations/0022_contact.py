# Generated by Django 4.0.5 on 2022-07-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_book_bk_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('cn_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cn_name', models.CharField(max_length=100)),
                ('cn_email', models.CharField(max_length=100)),
                ('cn_subject', models.CharField(max_length=100)),
                ('cn_message', models.CharField(max_length=100)),
                ('cn_status', models.IntegerField(default=0)),
                ('cn_created_at', models.DateTimeField(auto_now=True)),
                ('cn_created_by', models.CharField(max_length=100)),
            ],
        ),
    ]