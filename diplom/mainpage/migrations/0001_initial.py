# Generated by Django 5.0 on 2024-03-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.IntegerField()),
                ('tgid', models.IntegerField(null=True)),
            ],
        ),
    ]
