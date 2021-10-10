from django import forms
from django.core.validators import FileExtensionValidator

class StudentJsonForm(forms.Form):
    file_json = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['json'])])
