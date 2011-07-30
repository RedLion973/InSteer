from django import forms
from django.contrib.auth.models import User
from InSteer.ownership.models import ProjectActor
from InSteer.utils.fields import UserFullnameChoiceField

class ProjectActorForm(forms.ModelForm):
    user = UserFullnameChoiceField(queryset=User.objects.all())

    class Meta:
        model = ProjectActor