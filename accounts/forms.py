from .models import BusRegister
from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


from .models import User, BusRegister


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=300)
    email = forms.EmailField(label='email address')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Password do not match')
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if not username and email and password and password2:
            raise forms.ValidationError('please dont leave any box blank')
         # TODO Validation

        return super(UserRegistrationForm, self).clean(*args, **kwargs)


class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )

    def clean(self, *args, **kwargs):

        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')

        user_qs_final = User.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct()

        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError(
                'Invalid credentials - user does not exist')

        user_obj = user_qs_final.first()

        if not user_obj.check_password(password):
            raise forms.ValidationError('credentials are not correct')
        self.cleaned_data['user_obj'] = user_obj

        return super(UserLoginForm, self).clean(*args, **kwargs)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'image',
            'phone_number',
            'location',
        ]


class BusRegisterForm(forms.ModelForm):

    class Meta:
        model = BusRegister
        fields = [
            'picture_of_bus',
            'bus_plate_number',
            'number_of_sits',
            'location',
            'agreement',
        ]
