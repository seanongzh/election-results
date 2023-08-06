# Generated by Django 4.2.3 on 2023-08-06 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('is_special', models.BooleanField(default=False)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positions.position')),
            ],
        ),
        migrations.AddConstraint(
            model_name='election',
            constraint=models.CheckConstraint(check=models.Q(('year__lte', 2023)), name='year_lte_now'),
        ),
        migrations.AddConstraint(
            model_name='election',
            constraint=models.UniqueConstraint(models.F('position'), models.F('year'), models.F('is_special'), name='unique_election'),
        ),
        migrations.AlterField(
            model_name='election',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='special election'),
        ),
        migrations.AddField(
            model_name='election',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterModelOptions(
            name='election',
            options={'ordering': ['-year', 'position', 'is_special']},
        ),
    ]
