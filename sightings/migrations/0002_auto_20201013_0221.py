# Generated by Django 3.1.2 on 2020-10-13 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='approches',
            field=models.BooleanField(default=False, help_text='Approaches'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='chasing',
            field=models.BooleanField(default=False, help_text='Chasing'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='climbing',
            field=models.BooleanField(default=False, help_text='Climbing'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='eating',
            field=models.BooleanField(default=False, help_text='Eating'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='foraging',
            field=models.BooleanField(default=False, help_text='Foraging'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='indifferent',
            field=models.BooleanField(default=False, help_text='Indifferent'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='kuks',
            field=models.BooleanField(default=False, help_text='Kuks'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='location',
            field=models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), ('OTHER', 'Other')], default='OTHER', help_text='Location', max_length=50),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='moans',
            field=models.BooleanField(default=False, help_text='Moans'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='other_activities',
            field=models.CharField(default='None', help_text='Other Activities', max_length=100),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='primary_fur_color',
            field=models.CharField(default='None', help_text='Primary fur color', max_length=50),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='quaas',
            field=models.BooleanField(default=False, help_text='Quaas'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='running',
            field=models.BooleanField(default=False, help_text='Running'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='runs_from',
            field=models.BooleanField(default=False, help_text='Runs from'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='specific_location',
            field=models.CharField(default='None', help_text='Specific location', max_length=100),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='tail_flags',
            field=models.BooleanField(default=False, help_text='Tail Flags'),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='tail_switches',
            field=models.BooleanField(default=False, help_text='Tail Switches'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='unique_squirrel_id',
            field=models.CharField(default='None', help_text='Unique Squirrel ID', max_length=100),
        ),
    ]
