# Generated by Django 3.0.8 on 2020-08-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200805_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_var1',
            field=models.CharField(default='Q', max_length=50, verbose_name='елемент1'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_var2',
            field=models.CharField(default='Q', max_length=50, verbose_name='елемент2'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_var3',
            field=models.CharField(default='Q', max_length=50, verbose_name='елемент3'),
        ),
    ]
