# Generated by Django 3.0.8 on 2020-08-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200805_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_sim1',
            field=models.CharField(default='', max_length=10, verbose_name='символ1'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_sim2',
            field=models.CharField(default='', max_length=10, verbose_name='символ2'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_sim3',
            field=models.CharField(default='', max_length=10, verbose_name='символ3'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_sim4',
            field=models.CharField(default='', max_length=10, verbose_name='символ4'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_var4',
            field=models.CharField(default='', max_length=10, verbose_name='елемент4'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_var5',
            field=models.CharField(default='', max_length=10, verbose_name='елемент5'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_var6',
            field=models.CharField(default='', max_length=10, verbose_name='елемент6'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_var1',
            field=models.CharField(default='', max_length=10, verbose_name='елемент1'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_var2',
            field=models.CharField(default='', max_length=10, verbose_name='елемент2'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_var3',
            field=models.CharField(default='', max_length=10, verbose_name='елемент3'),
        ),
    ]
