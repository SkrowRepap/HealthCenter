# Generated by Django 3.2.7 on 2021-10-12 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_patients_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='patient_id',
            field=models.AutoField(db_column='patient_ID', primary_key=True, serialize=False),
        ),
    ]