# Generated by Django 3.1.3 on 2020-12-02 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20201202_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 19, 11, 59, 327965)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 19, 11, 59, 327965)),
        ),
    ]
