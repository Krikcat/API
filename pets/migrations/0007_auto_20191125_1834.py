# Generated by Django 2.2.7 on 2019-11-25 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_auto_20191124_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='pets',
            name='price',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pets',
            name='bye',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pets.Bye'),
        ),
    ]
