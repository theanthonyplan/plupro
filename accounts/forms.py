from django import forms
from django.contrib.auth.models import User
#inheriting from UserCreationForm
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		)

		def save(self):
			user = super(RegistrationForm, self).save(commit=False)
			user.first_name = self.cleaned_date['first_name']
			user.last_name = self.cleaned_date['last_name']
			user.email = self.cleaned_date['email']

			if commit:
				user.save()
			return user

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = (
			'first_name',
			'last_name',
			'email',
			'password',
			)

class EditUserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = (
			'title',
			'city',
			'country',
			'phone_number',
		)
