# Generated by Django 3.0.8 on 2020-08-05 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='coment',
            new_name='Comment',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'стаття', 'verbose_name_plural': 'статті'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'коментар', 'verbose_name_plural': 'коментарі'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='coment_text',
            new_name='comment_text',
        ),
    ]
