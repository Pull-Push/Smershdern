# Generated by Django 5.0.6 on 2024-06-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskeywheel', '0003_ww_member_date_created_ww_member_date_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='ww_member',
            name='member_id',
            field=models.IntegerField(default=99),
            preserve_default=False,
        ),
    ]
