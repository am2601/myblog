from django import forms
from .models import FeedBack


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('email', 'title', 'text')
