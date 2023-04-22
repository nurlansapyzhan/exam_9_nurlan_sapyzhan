from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='', strip=False, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password_confirm = forms.CharField(label='', strip=False, required=True,
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'password', 'password_confirm'
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords mismatch")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


