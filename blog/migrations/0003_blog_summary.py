# Generated by Django 2.2.4 on 2019-09-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190927_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]