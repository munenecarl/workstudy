# Generated by Django 4.1.3 on 2023-02-02 06:01

import assets.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='item name')),
                ('pic', models.ImageField(
                    upload_to=assets.models.asset_photo_upload, verbose_name=' asset image')),
                ('status', models.CharField(choices=[('Not available', ' Not available'), (
                    'Available', 'Available'), ('Borrowed', 'Borrowed')], max_length=50, verbose_name='asset status')),
                ('condition', models.CharField(choices=[('Good', 'Good'), ('Not Woking', 'Not Working'), (
                    'Faulty', 'Faulty')], max_length=50, verbose_name='asset condition')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='organizations.organization', verbose_name='lab / organization')),
            ],
            options={
                'verbose_name': 'Asset',
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='Borrowd_Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=50,
                 verbose_name='borrowers name(one)')),
                ('contacts', models.CharField(
                    max_length=50, verbose_name='borrowers contact')),
                ('location_of_use', models.CharField(
                    max_length=50, verbose_name='Class/Hall')),
                ('picked_on', models.DateTimeField(
                    editable=False, verbose_name='date and time picked')),
                ('returned_on', models.DateTimeField(blank=True,
                 null=True, verbose_name='date and time returned')),
                ('returned', models.BooleanField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='assets.asset', verbose_name='borrowed item')),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='organizations.organization', verbose_name='lab')),
            ],
            options={
                'verbose_name': 'Borrowd Asset',
                'verbose_name_plural': 'Borrowd Assets',
                'ordering': ['returned_on'],
            },
        ),
    ]
