# Generated by Django 2.0.8 on 2018-08-14 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0014_configcontexts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraction',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='useraction',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAction',
        ),
    ]
