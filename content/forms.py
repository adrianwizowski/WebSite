from django import forms

from .models import Post, Donation

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)



class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = ('name',)