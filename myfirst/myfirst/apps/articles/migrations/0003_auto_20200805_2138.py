# Generated by Django 3.0.8 on 2020-08-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200805_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.CharField(max_length=100, verbose_name='формула'),
        ),
    ]
