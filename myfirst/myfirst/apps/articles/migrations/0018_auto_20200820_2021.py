# Generated by Django 3.0.8 on 2020-08-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20200820_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obj',
            old_name='obj_topic',
            new_name='obj_topic1',
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic10',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic11',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic12',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic2',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic3',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic4',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic5',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic6',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic7',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic8',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
        migrations.AddField(
            model_name='obj',
            name='obj_topic9',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='тема'),
        ),
    ]
