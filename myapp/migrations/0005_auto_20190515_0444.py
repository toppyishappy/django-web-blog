# Generated by Django 2.2.1 on 2019-05-15 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_commentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.BlogModel'),
        ),
    ]