# Generated by Django 4.1.3 on 2023-07-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_alter_asset_condition_alter_asset_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='condition',
            field=models.CharField(choices=[('Not Woking', 'Not Working'), ('Good', 'Good'), ('Faulty', 'Faulty')], max_length=50, verbose_name='asset condition'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('Not available', ' Not available'), ('Borrowed', 'Borrowed'), ('Available', 'Available'), ('Pending Approval', 'Pending Approval')], max_length=50, verbose_name='asset status'),
        ),
        migrations.AlterField(
            model_name='assetcategory',
            name='category',
            field=models.TextField(choices=[('VGA Cables', 'VGA Cables'), ('HDMI Cables', 'HDMI Cables'), ('Projector', 'Projector'), ('Others', 'Others'), ('Extension/Power Cables', 'Extension/Power Cables'), ('VGA-HDMI Converters', ' VGA-HDMI Converters'), ('Remote', 'Remote')], max_length=50, verbose_name='Asset category name'),
        ),
    ]
