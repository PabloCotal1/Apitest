# Generated by Django 5.0.6 on 2024-05-10 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.PositiveIntegerField(default=0)),
                ('modelo', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=100)),
                ('códigodeproducto', models.PositiveIntegerField(default=0)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
