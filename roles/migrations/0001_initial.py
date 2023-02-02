# Generated by Django 4.1.3 on 2023-02-02 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0002_alter_issue_status'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=250, null=True, verbose_name='role description')),
                ('task_1', models.CharField(blank=True, max_length=200, null=True, verbose_name='task 1')),
                ('task_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='task 2')),
                ('task_3', models.CharField(blank=True, max_length=200, null=True, verbose_name='task 3')),
                ('task_4', models.CharField(blank=True, max_length=200, null=True, verbose_name='task 4')),
                ('task_5', models.CharField(blank=True, max_length=200, null=True, verbose_name='task 5')),
                ('task_6', models.CharField(blank=True, max_length=200, null=True, verbose_name='task 6')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization', verbose_name='Organization')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day1', models.CharField(blank=True, choices=[('Thurday', 'Thursday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday')], max_length=15, null=True)),
                ('day1_start_time', models.TimeField(blank=True, null=True)),
                ('day1_end_time', models.TimeField(blank=True, null=True)),
                ('day2', models.CharField(blank=True, choices=[('Thurday', 'Thursday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday')], max_length=15, null=True)),
                ('day2_start_time', models.TimeField(blank=True, null=True)),
                ('day2_end_time', models.TimeField(blank=True, null=True)),
                ('day3', models.CharField(blank=True, choices=[('Thurday', 'Thursday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday')], max_length=15, null=True)),
                ('day3_start_time', models.TimeField(blank=True, null=True)),
                ('day3_end_time', models.TimeField(blank=True, null=True)),
                ('day4', models.CharField(blank=True, choices=[('Thurday', 'Thursday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday')], max_length=15, null=True)),
                ('day4_start_time', models.TimeField(blank=True, null=True)),
                ('day4_end_time', models.TimeField(blank=True, null=True)),
                ('day5', models.CharField(blank=True, choices=[('Thurday', 'Thursday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday')], max_length=15, null=True)),
                ('day5_start_time', models.TimeField(blank=True, null=True)),
                ('day5_end_time', models.TimeField(blank=True, null=True)),
                ('day6', models.CharField(blank=True, choices=[('Thurday', 'Thursday'), ('Saturday', 'Saturday'), ('Tuesday', 'Tuesday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday')], max_length=15, null=True)),
                ('day6_start_time', models.TimeField(blank=True, null=True)),
                ('day6_end_time', models.TimeField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.account', verbose_name='assigned_to')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roles.role', verbose_name='role')),
            ],
            options={
                'verbose_name': "User's role",
                'verbose_name_plural': "User's  roles",
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_1', models.TextField(blank=True, max_length=100, null=True, verbose_name='task 1')),
                ('task_2', models.TextField(blank=True, max_length=100, null=True, verbose_name='task 2')),
                ('task_3', models.TextField(blank=True, max_length=100, null=True, verbose_name='task 3')),
                ('task_4', models.TextField(blank=True, max_length=100, null=True, verbose_name='task 4')),
                ('task_5', models.TextField(blank=True, max_length=100, null=True, verbose_name='task 5')),
                ('task_6', models.TextField(blank=True, max_length=100, null=True, verbose_name='task 6')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roles.role', verbose_name='Role')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
