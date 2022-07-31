from django import forms
from .models import ReviewModel
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = ReviewModel
        # fields = ['first_name', 'last_name', 'stars']
        fields = "__all__"

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "stars": "Rate"
        }

        error_messages = {
             'stars': {
                 'min_value': 'Min value is 0',
                 'max_value': 'Max value is 5'
             }
        }


