from django import forms
from django.forms import ValidationError
from .models import Student
from django.forms.widgets import RadioSelect

class AddStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        #fields = ["mobile", "email" ]
        widgets = {
          'gender': RadioSelect,
        }
