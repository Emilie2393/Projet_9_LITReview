from django import forms
from . import models
from django.contrib.auth import get_user_model


User = get_user_model()


"""class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']"""
class ToFollow(forms.Form):
    to_follow = forms.CharField(widget=forms.HiddenInput)

class ReviewForm(forms.ModelForm):
    post_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        CHOICES = [(i, i) for i in range(1, 6)]
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'rating': forms.RadioSelect(choices=CHOICES),
        }

class TicketForm(forms.ModelForm):
    edit_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Ticket
        fields = ['title', 'image', 'description']

class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class UnSubscribe(forms.Form):
    unsubscribe = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    