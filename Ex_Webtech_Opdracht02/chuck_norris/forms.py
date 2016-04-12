from django import forms

class NameForm(forms.Form):
	first_name = forms.CharField(label='Firstname ', max_length=100)
	last_name = forms.CharField(label='Lastname ', max_length=100)
	