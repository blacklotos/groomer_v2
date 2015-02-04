from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
#clas formu logina
class LoginForm(forms.Form):
    #polya
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

#proverka logina
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Wrong username')
        return username

#proverka password
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError('Invalid Password')
        elif user is None:
            pass
        else:
            return password

#clas formu registracii
class RegistrationForm (forms.ModelForm):
    #dopolnitelnue polya
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Re-enter Password',widget=forms.PasswordInput())
    is_groomer = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    #proverka parolya2 sovpadaet li s pervum
    def clean_pssword2(self):
        password1 = self.cleaned_data.get('username1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not math.')
        return password2

    #proverka na unikalnost emaila
    def clean_email(self):
        email = self.cleaned_data.get('email')
        #podschet skolko takih emaylov est
        user_count = User.objects.filter(email=email).count()
        #proverka eli email ispolzovalsya pri registracii vuvesti oshibku
        if user_count > 0:
            raise forms.ValidationError('This email alredy used.')
        return email

    #Sohraneniya registracii v bazu
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user
