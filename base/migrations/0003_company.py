# Generated by Django 4.2.6 on 2023-10-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_advocate_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
