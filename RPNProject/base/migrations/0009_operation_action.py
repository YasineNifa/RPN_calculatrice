# Generated by Django 4.1 on 2022-09-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_stackmodel_new_remove_stackmodel_old_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='action',
            field=models.TextField(blank=True, null=True),
        ),
    ]
