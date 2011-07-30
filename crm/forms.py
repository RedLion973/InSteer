from django import forms
from django.contrib.auth.models import User
from InSteer.crm.models import Client
from InSteer.utils.fields import UserFullnameChoiceField

class ClientForm(forms.ModelForm):
    user = UserFullnameChoiceField(queryset=User.objects.all())

    class Meta:
        model = Client