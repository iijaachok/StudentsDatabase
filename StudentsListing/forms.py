from django import forms
from StudentsListing.models import Group, Student


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student


class Confirm(forms.Form):
    choice = forms.BooleanField(widget=forms.HiddenInput(),
                                initial=True,
                                required=False,
                                label=u'Delete?')