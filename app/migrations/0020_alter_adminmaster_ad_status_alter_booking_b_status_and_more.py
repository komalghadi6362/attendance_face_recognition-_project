# Generated by Django 4.0.5 on 2022-07-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmaster',
            name='ad_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='b_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='ct_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='em_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hall',
            name='h_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='sp_status',
            field=models.IntegerField(default=0),
        ),
    ]
