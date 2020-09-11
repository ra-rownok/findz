# Generated by Django 3.1.1 on 2020-09-11 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tutorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.tutorial'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_type',
            field=models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], max_length=50),
        ),
    ]