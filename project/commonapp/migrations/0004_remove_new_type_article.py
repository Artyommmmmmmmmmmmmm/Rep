# Generated by Django 4.2.6 on 2023-11-09 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0003_new_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='type',
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('text', models.TextField()),
                ('made_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Articles', to='commonapp.category')),
            ],
        ),
    ]