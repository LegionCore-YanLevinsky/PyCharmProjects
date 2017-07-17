from django.contrib.auth.forms import UserCreationForm, User


class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name')
