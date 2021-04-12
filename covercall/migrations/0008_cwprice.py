# Generated by Django 3.0.2 on 2021-04-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covercall', '0007_auto_20210406_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='CWPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCW', models.DateField()),
                ('symbolCW', models.CharField(max_length=10)),
                ('openPriceCW', models.FloatField(null=True)),
                ('highPriceCW', models.FloatField(null=True)),
                ('lowPriceCW', models.FloatField(null=True)),
                ('closePriceCW', models.FloatField(null=True)),
                ('volumeCW', models.FloatField(null=True)),
                ('valueCW', models.FloatField(null=True)),
            ],
        ),
    ]
