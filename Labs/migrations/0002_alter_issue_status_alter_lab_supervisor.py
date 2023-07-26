# Generated by Django 4.1.3 on 2023-07-22 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '__first__'),
        ('Labs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('Medium attention', 'Medium attention'), ('Urgent attention', 'Urgent attention'), ('Done', 'Done'), ('Noted pending address', 'Noted pending address'), ('Addressing', 'Addressing'), ('Low attention', 'Low attention')], max_length=50, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='supervisor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Lab', to='accounts.account', verbose_name="Lab's creater"),
        ),
    ]
