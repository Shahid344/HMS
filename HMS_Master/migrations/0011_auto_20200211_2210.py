# Generated by Django 2.2.1 on 2020-02-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS_Master', '0010_auto_20200211_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_pan_no',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]