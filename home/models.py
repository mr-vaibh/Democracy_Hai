from django.db import models

# Create your models here.

class Reports():
    name = models.CharField(max_length=255)
    gender = models.ChoiceField(choices=["Male", "Female", "Transgender", "Others (If a group/organisation)"])
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.IntegerField()
    email = models.EmailField(max_length=255)
    phoneno = models.PhoneNumberField()
    category = models.ChoiceField(choices=["Public Grievances", "Suggestion/Feedback", "Financial Fraud/Scam", "Greetings/Wishes", "Appointment with PM", "Message Requests"])
    query = models.CharField(max_length=5000)
    identity_no = models.CharField(max_length=100)
    identity_doc = models.FileField(upload_to='/media/reports/identities')
    user_upload = models.FileField(upload_to='/media/reports/useruploads')
    reviewed = models.BooleanField(default=False)
    fulfilled = models.BooleanField(default=False)