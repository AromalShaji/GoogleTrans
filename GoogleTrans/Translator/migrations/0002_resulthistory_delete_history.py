# Generated by Django 5.0.2 on 2024-03-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Translator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resultHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('text', models.CharField(default='', max_length=50)),
                ('result', models.CharField(max_length=50)),
                ('date', models.DateField(default='1')),
            ],
        ),
        migrations.DeleteModel(
            name='history',
        ),
    ]
