# Generated by Django 3.1.7 on 2021-03-21 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envelope', '0006_auto_20210321_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-created',), 'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]
