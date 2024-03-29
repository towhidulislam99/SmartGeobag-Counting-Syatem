# Generated by Django 4.2.5 on 2024-02-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Geobag_Counting', '0002_alter_prototypeproposed_proposed_figure_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToonificationHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toonification_heading', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ToonificationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toonification_photo', models.ImageField(default='No images', upload_to='ToonificationImage/')),
            ],
        ),
    ]
