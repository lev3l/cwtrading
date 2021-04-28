# Generated by Django 3.0.2 on 2021-04-28 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covercall', '0012_auto_20210428_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backtest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enddateBt', models.DateField()),
                ('timerange', models.FloatField(null=True)),
                ('c', models.FloatField(null=True)),
                ('m', models.FloatField(null=True)),
                ('n', models.FloatField(null=True)),
            ],
        ),
    ]
