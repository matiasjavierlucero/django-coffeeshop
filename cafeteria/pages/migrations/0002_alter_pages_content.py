# Generated by Django 3.2.7 on 2021-09-10 19:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]
