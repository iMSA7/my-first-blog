from django import forms

from .models import Post, Cv

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CvForm(forms.ModelForm):

	class Meta:
		model = Cv
		fields = ('name','address','telephone','mobile','email','summary','skills','education','work','voluntary', 'interests', 'referees')
			
		