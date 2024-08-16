from django.forms import ModelForm
# from django.contrib.auth.forms import UserModel , UserCreationForm , AuthenticationForm
from .models import PersonalInfo , ClientRegister
from django import forms
from django.core import validators
from django.forms import widgets
from django.contrib.auth.models import User

class Student(ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['name' , 'std_id' , 'email' , 'mobile_num' , 'address']


class AllCoveredForm(forms.Form):
    # Text input fields
    char_field = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Text Input'}))
    password_field = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email_field = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    url_field = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'URL'}))

    # Number input fields
    integer_field = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Integer'}))
    float_field = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Float'}))

    # Date and time fields
    date_field = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time_field = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    datetime_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    # Select fields
    choice_field = forms.ChoiceField(choices=[('1', 'Option 1'), ('2', 'Option 2')], widget=forms.Select)
    multiple_choice_field = forms.MultipleChoiceField(choices=[('1', 'Option 1'), ('2', 'Option 2')], widget=forms.CheckboxSelectMultiple)

    # Boolean field
    boolean_field = forms.BooleanField(widget=forms.CheckboxInput, required=False)

    # File input field
    file_field = forms.FileField(widget=forms.ClearableFileInput)

    # Radio buttons
    radio_choice_field = forms.ChoiceField(choices=[('1', 'Option 1'), ('2', 'Option 2')], widget=forms.RadioSelect)

    # Textarea
    textarea_field = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter text here...'}))

    # Hidden field
    hidden_field = forms.CharField(widget=forms.HiddenInput, initial='hidden_value')

    # Slug field (used for SEO-friendly URLs)
    slug_field = forms.SlugField(widget=forms.TextInput(attrs={'placeholder': 'Slug'}))

    # IP Address field
    ip_field = forms.GenericIPAddressField(widget=forms.TextInput(attrs={'placeholder': 'IP Address'}))

    # # File Path field (used for selecting files from server directory)
    # file_path_field = forms.FilePathField(path="home/", widget=forms.Select)

    # NullBooleanField (used to represent three states: True, False, and None)
    null_boolean_field = forms.NullBooleanField(widget=forms.Select(choices=[(None, 'Unknown'), (True, 'Yes'), (False, 'No')]))

class another(forms.Form):
    name = forms.CharField(max_length=100 , label='Your Nice NAme')
    id = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder' : 'Enter Id'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}) , validators=[validators.MinLengthValidator(8)])
    second_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Enter PassWord Again'}))

    # def clean_password(self):
    #     clean_pass = self.cleaned_data.get('password')
    #     if len(clean_pass) < 8:
    #         raise forms.ValidationError('Password Too Short')
    #     return clean_pass

    def clean(self):
        cleaned_data = super().clean()
        pas1 = cleaned_data.get('password')
        pas2 = cleaned_data.get('second_pass')

        if pas1 and pas2 and pas1 != pas2:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password')

class ClientRegisterForm(forms.ModelForm):
    # profile_url = forms.URLField(required=False)
    # profile_pic = forms.ImageField(required=False)

    class Meta:
        model = ClientRegister
        fields = ('profile_url' , 'profile_pic')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20 , required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : 'Write Your Message Here '}))