# Generated by Django 2.2.1 on 2019-05-23 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190515_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
