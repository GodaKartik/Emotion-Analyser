# Generated by Django 4.1.3 on 2022-12-05 08:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('miniProject', '0002_rename_tht_thought_thoughts'),
    ]

    operations = [
        migrations.AddField(
            model_name='thought',
            name='uid',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
