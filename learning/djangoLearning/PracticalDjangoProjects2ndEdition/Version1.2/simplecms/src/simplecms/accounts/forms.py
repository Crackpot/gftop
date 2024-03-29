#coding=utf8
from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length = 30)
    email = forms.EmailField()
    password1 = forms.CharField(max_length = 30,
            widget = forms.PasswordInput(render_value = False))
    password2 = forms.CharField(max_length = 30,
            widget = forms.PasswordInput(render_value = False))

    def clean_username(self):
        try:
            User.objects.get(username = self.cleaned_data['username'])
        except User.DoesNotExist:
            # 用户不存在是进行注册的前提
            return self.cleaned_data['username']
        raise forms.ValidationError("This username is already in use. Please choose another.")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("You must type the same password each time")
        return self.cleaned_data

    def save(self):
        new_user = User.objects.create_user(username = self.cleaned_data['username'], # 该方法自动处理密码
                email = self.cleaned_data['email'],
                password = self.cleaned_data['password1'])
        return new_user
