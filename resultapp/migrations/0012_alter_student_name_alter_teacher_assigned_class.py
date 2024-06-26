# Generated by Django 5.0.3 on 2024-03-25 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultapp', '0011_remove_class_teacher_remove_student_class_obj_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='assigned_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resultapp.class', unique=True),
        ),
    ]
