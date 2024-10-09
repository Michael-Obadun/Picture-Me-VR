from .models import Comment, Meeting
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('author','platform','venue', 'discription','start_time',)

