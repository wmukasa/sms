from django import forms


class CreateSms(forms.Form):
    message = forms.CharField(
                        label='message',
                        max_length=255,
                        min_length=3,
                        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5, "cols": 20}))  # noqa: E501
