from django.contrib.auth.models import User

from .models import Profile, Part, Car
from django import forms


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # this is the magic right here:
        self.fields['email'].label = "E.mail"
        self.fields['first_name'].label = "Name"
        self.fields['last_name'].label = "Last name"
        self.fields[
            'email'].help_text = "Make sure you enter a valid email, otherwise you won't be able to reset your password!"


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cover', 'city', 'address', 'phone_number']


class UserPartCreateForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['status', 'part_picture', 'part_picture_2', 'part_picture_3', 'part_picture_4', 'part_oem',
                  'part_name', 'part_description',
                  'side', 'condition', 'part_type', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['part_picture'].label = "Main Cover"
        self.fields['part_picture_2'].label = "Cover"
        self.fields['part_picture'].help_text = "If will be uploaded 1 img,last 3 will be no img"
        self.fields['part_picture_3'].label = "Cover"
        self.fields['part_picture_4'].label = "Cover"
        self.fields[
            'part_name'].help_text = "Its import for search. (Part-OEM,Car-brand,Car-mark,years,and part name(A1231111 Audi A6 2020 Led Headlight))"
        self.fields['side'].help_text = "If part have side choose, if not leave ----"
        self.fields[
            'part_type'].help_text = "Important to choose part type ,because if you choose body part at part show color code "
        self.fields['price'].help_text = "Write price"


class UserCarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_cover', 'car_model', 'years', 'fuel', 'engine', 'engine_code',
                  'power', 'gearbox', 'gearbox_code', 'color', 'body_type', 'parts']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car_cover'].label = "Main Cover"
        self.fields['car_model'].label = "Car Model"


