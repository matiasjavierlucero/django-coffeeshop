# Generated by Django 3.2.7 on 2021-09-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-Created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.ImageField(upload_to='services'),
        ),
    ]
