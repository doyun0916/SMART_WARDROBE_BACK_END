# Generated by Django 3.1 on 2020-11-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0007_auto_20201102_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outerthick',
            name='brand',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='outerthick',
            name='descript',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='toplong',
            name='brand',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='toplong',
            name='descript',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
