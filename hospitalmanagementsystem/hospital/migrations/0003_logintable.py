# Generated by Django 4.1.1 on 2022-10-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_patient_bloodgroup_alter_patient_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csrfmiddlewaretoken', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
