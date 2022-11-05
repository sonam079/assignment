from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# I have taken following into consideration
# Country code (1 to 3 digits)
# Subscriber number (max 12 digits)
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. "
                                     "Up to 15 digits allowed.")

POLICY_STATUS_CHOICES = (
    ('requirements_awaited', 'Requirements Awaited'),
    ('requirements_closed', 'Requirements Closed'),
    ('underwriting', 'Underwriting'),
    ('policy_issued', 'Policy Issued'),
    ('policy_rejected', 'Policy Rejected'),
)

MEDICAL_TYPE_CHOICES = (
    ('tele_medicals', 'Tele Medicals'),
    ('physical_medicals', 'Physical Medicals'),
)

MEDICAL_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('schedules', 'Scheduled'),
    ('waiting_for_report', 'Waiting for Report'),
    ('done', 'Done'),
)


# Create your models here.
class AbsTractCreatedUpdated(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LifePolicy(AbsTractCreatedUpdated):
    application_number = models.CharField(max_length=10, validators=[alphanumeric])
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=17, null=False, blank=False, validators=[phone_regex])
    date_of_birth = models.DateField(null=True, blank=True)
    policy_cover = models.IntegerField(null=True, blank=True)
    policy_status = models.CharField(max_length=50, choices=POLICY_STATUS_CHOICES, null=True, blank=True)
    policy_number = models.IntegerField()
    medical_type = models.CharField(max_length=50, choices=MEDICAL_TYPE_CHOICES)
    medical_status = models.CharField(max_length=50, choices=MEDICAL_STATUS_CHOICES)
    remarks = models.CharField(max_length=200)





