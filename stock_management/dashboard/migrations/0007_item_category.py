# Generated by Django 2.0.7 on 2018-10-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20181024_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
