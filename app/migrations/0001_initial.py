# Generated by Django 5.0.2 on 2024-03-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scname', models.CharField(max_length=100)),
                ('sprincipal', models.CharField(max_length=100)),
                ('slocation', models.CharField(max_length=100)),
            ],
        ),
    ]
