# Generated by Django 3.2.7 on 2021-09-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('phoneNumber', models.CharField(max_length=15)),
                ('retryCount', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('networkCode', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Delivery Report',
                'verbose_name_plural': 'Delivery Reports',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('text', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('to', models.IntegerField()),
                ('linkId', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Inbox',
                'verbose_name_plural': 'Inbox',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Outbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('statusCode', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('text', models.CharField(max_length=255)),
                ('messageId', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Outbox',
                'verbose_name_plural': 'Outbox',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='phoneNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
