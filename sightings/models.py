from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):
    latitude = models.FloatField(
        help_text=_('Latitude')
    )    

    longitude = models.FloatField(
        help_text=_('Longitude')
    )

    unique_squirrel_id = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=100,
        default='None',
    )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    shift = models.CharField(
        help_text=_('Shift'),
        choices=SHIFT_CHOICES,
        default=AM,
        max_length=2,
    )

    date = models.DateField(
        help_text=_('Date'),
    )

    ADULT = 'ADULT'
    JUVENILE = 'JUVENILE'
    OTHER = 'OTHER'
    AGE_CHOICES = (
        (ADULT, 'ADULT'),
        (JUVENILE, 'JUVENILE'),
        (OTHER, 'OTHER'),
    )

    age = models.CharField(
        help_text=_('Age'),
        choices=AGE_CHOICES,
        default=ADULT,
        max_length=10,
    )
    
    primary_fur_color = models.CharField(
        help_text=_('Primary fur color'),
        max_length=50,
        default='None',
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
        (OTHER, 'Other'),
    )
    location = models.CharField(
        help_text=_('Location'),
        choices=LOCATION_CHOICES,
        default=OTHER,
        max_length=50,
    )

    specific_location = models.CharField(
        help_text=_('Specific location'),
        max_length=100,
        default='None',
    )

    running = models.BooleanField(
        help_text=_('Running'),
        default=False
    )

    chasing = models.BooleanField(
        help_text=_('Chasing'),
        default=False
    )

    climbing = models.BooleanField(
        help_text=_('Climbing'),
        default=False
    )

    eating = models.BooleanField(
        help_text=_('Eating'),
        default=False
    )

    foraging = models.BooleanField(
        help_text=_('Foraging'),
        default=False
    )

    other_activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=100,
        default='None',
    )

    kuks = models.BooleanField(
        help_text=_('Kuks'),
        default=False
    )

    quaas = models.BooleanField(
        help_text=_('Quaas'),
        default=False
    )

    moans = models.BooleanField(
        help_text=_('Moans'),
        default=False
    )

    tail_flags = models.BooleanField(
        help_text=_('Tail Flags'),
        default=False
    )

    tail_switches = models.BooleanField(
        help_text=_('Tail Switches'),
        default=False
    )

    approaches = models.BooleanField(
        help_text=_('Approaches'),
        default=False
    )

    indifferent = models.BooleanField(
        help_text=_('Indifferent'),
        default=False
    )

    runs_from = models.BooleanField(
        help_text=_('Runs from'),
        default=False
    )

    def __str__(self):
        return self.unique_squirrel_id
