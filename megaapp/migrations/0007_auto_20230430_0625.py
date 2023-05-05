# Generated by Django 3.2.9 on 2023-04-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megaapp', '0006_auto_20230430_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffe',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='coffebrand',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='coffecategory',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='glass',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='glassbrand',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='glasscategory',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='watch',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='watchbrand',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='watchcategory',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]