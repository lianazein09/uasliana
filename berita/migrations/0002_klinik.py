# Generated by Django 4.2.6 on 2024-01-02 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='klinik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_klinik', models.CharField(max_length=100)),
            ],
        ),
    ]
