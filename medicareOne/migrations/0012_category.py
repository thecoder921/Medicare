# Generated by Django 2.2.4 on 2020-06-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicareOne', '0011_infrasturcture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(default='', max_length=50, verbose_name='Category')),
                ('image', models.ImageField(default='', upload_to='Category/Images', verbose_name='Image')),
            ],
        ),
    ]
