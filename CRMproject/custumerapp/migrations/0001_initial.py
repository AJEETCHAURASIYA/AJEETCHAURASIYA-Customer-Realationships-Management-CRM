# Generated by Django 5.0.4 on 2024-05-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=10)),
                ('emailaddress', models.CharField(max_length=50)),
                ('responsetype', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=500)),
                ('responsetext', models.CharField(max_length=5000)),
                ('posteddate', models.CharField(max_length=30)),
            ],
        ),
    ]
