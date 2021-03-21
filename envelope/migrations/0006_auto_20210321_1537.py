# Generated by Django 3.1.7 on 2021-03-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envelope', '0005_auto_20210321_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AddField(
            model_name='message',
            name='raw_message',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
