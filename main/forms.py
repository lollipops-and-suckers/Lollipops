from django import forms
from .models import ContactProfile, Notification


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Your Name',
			'id': 'name',
			'class': 'form-control'
			}))
	email = forms.EmailField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Your Email',
			'id': 'email',
			'class': 'form-control'
			}))
	subject = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Subject',
			'id': 'subject',
			'class': 'form-control'
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Message',
			'id': 'message',
			'class': 'form-control',
			'rows': 5,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'subject', 'message',)

class Notification(forms.ModelForm):
	
	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Your name',
			'class': 'form-control'
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Your Email',
			'class': 'form-control'
			}))


	class Meta:
		model = Notification
		fields = ('name', 'email',)	