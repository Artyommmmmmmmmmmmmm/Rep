# Generated by Django 4.2.6 on 2023-11-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0002_new_made_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='type',
            field=models.CharField(choices=[('AR', 'Статья'), ('NE', 'Новость')], default='NE', max_length=2),
        ),
    ]