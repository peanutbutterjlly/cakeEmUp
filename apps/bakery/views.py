from datetime import date, timedelta

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django import forms
from django.utils import dateformat

from .models import CustomerSubmission

two_weeks_out = date.today() + timedelta(days=14)

example_date = dateformat.format(
    two_weeks_out, "D, F jS"
)  # to use in the help text of the form


def present_or_future_date(value):
    """validator to prevent picking a date earlier than 2 weeks out in the form"""
    if value < two_weeks_out:
        raise forms.ValidationError("The date can't be earlier than two weeks")
    return value


class SubmitForm(forms.ModelForm):
    """make a form created for the submit request"""

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        help_text="(Optional)",
    )
    date_needed = forms.DateField(
        help_text=f"(Optional) Please select a date at least 2 weeks out; e.g.: {example_date}",
        validators=[present_or_future_date],
        widget=forms.DateInput(
            attrs={
                "class": "datepicker",
                "type": "date",
            }
        ),
        required=False,
    )
    delivery = forms.BooleanField(required=False, help_text="(Optional)")
    topyenoh = forms.CharField(
        widget=forms.HiddenInput, required=False, label="leave empty"
    )
    name_field = forms.CharField(max_length=100, label="Name")
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = CustomerSubmission
        fields = [
            "name",
            "email",
            "phone",
            "message",
            "delivery",
            "date_needed",
            "image",
        ]

    def clean_topyenoh(self):
        topyenoh = self.cleaned_data["topyenoh"]
        if len(topyenoh):
            raise forms.ValidationError("honeypot should be left empty. Bad bot!")
        return topyenoh
