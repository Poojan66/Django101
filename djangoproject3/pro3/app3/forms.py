from django import forms

class formname(forms.Form):
	name=forms.CharField()
	email=forms.email()
	text=forms.CharField(widget=forms.Textarea)
