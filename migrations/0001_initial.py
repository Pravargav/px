# Generated by Django 4.1.2 on 2022-10-19 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('dob', models.DateTimeField(verbose_name='date of birth')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=200)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.student_register')),
            ],
        ),
    ]
