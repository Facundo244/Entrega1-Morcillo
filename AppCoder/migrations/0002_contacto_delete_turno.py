# Generated by Django 4.0.4 on 2022-06-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.IntegerField()),
                ('localidad', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Turno',
        ),
    ]
