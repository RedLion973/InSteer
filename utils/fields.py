from django import forms
from django.utils.encoding import smart_unicode

class UserFullnameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return smart_unicode(obj.get_full_name())