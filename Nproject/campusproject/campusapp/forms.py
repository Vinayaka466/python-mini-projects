from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'course']

class UpdateAgeForm(forms.Form):
    age = forms.IntegerField(min_value=0)
