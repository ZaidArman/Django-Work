# Generated by Django 4.2.7 on 2024-02-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDapp', '0003_alter_student_entry_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_entry',
            name='roll_no',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
    ]
