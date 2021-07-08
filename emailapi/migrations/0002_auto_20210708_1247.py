# Generated by Django 3.2.5 on 2021-07-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emailname', models.EmailField(max_length=200)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]