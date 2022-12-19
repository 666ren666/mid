from django.forms import ModelForm 
from cards.models import UserProfile

class LoginForm(ModelForm):

	class Meta:
		model=UserProfile
		fields='name', 'password'



class SigninForm(ModelForm):

	class Meta:
		model=UserProfile
		fields='name', 'password'


