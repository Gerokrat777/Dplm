from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите ваше имя пользователя'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'form-control',
                                          'placeholder': 'Введите ваш пароль'})
    )
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            # 'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    # last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            # 'last_name',
            'username',
            'email',
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    # last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
