# Generated by Django 2.2.1 on 2019-05-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20190515_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='tel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=20)),
            ],
        ),
    ]
