# Generated by Django 3.1.2 on 2021-03-01 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0002_auto_20210102_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='10B', max_length=20, verbose_name='клас')),
                ('ball', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='оцінка')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eng.test')),
            ],
            options={
                'verbose_name': 'оцінка',
                'verbose_name_plural': 'оцінки',
            },
        ),
    ]
