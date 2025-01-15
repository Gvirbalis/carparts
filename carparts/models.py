from django.contrib.auth.models import User
from django.db import models
from PIL import Image


# Create your models here.
class CarModel(models.Model):
    brand = models.CharField('Brand', null=True, max_length=100, help_text='Input Brand example(Ford)')
    model = models.CharField('Model', null=True, max_length=100, help_text='Input Model name example(Focus)')

    def __str__(self):
        return f'{self.brand} {self.model}'


class Car(models.Model):
    car_cover = models.ImageField('Cover', default="part_pics/no-image.jpg", upload_to='covers', null=True)
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE, null=True)
    years = models.CharField('Years', max_length=4, null=True, help_text='Input made date example(2020)')
    FUEL_CHOOSE = (
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
        ('choose', 'Unknown')
    )

    fuel = models.CharField(
        max_length=20,
        choices=FUEL_CHOOSE,
        blank=True,
        default='choose',
        help_text='Choose Fuel type',
    )

    engine = models.CharField('Engine', max_length=100, help_text='Input Brand example(2.0TDI)')
    engine_code = models.CharField('Engine Code', blank=True, max_length=100, help_text='Input Engine code')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    power = models.IntegerField('Power KW', help_text='Input power example(77)')
    GEARBOX_CHOOSE = (
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
        ('Unknown', 'Unknown')
    )
    gearbox = models.CharField(
        max_length=20,
        choices=GEARBOX_CHOOSE,
        blank=True,
        default='Unknown',
        help_text='Choose gearbox type',
    )

    gearbox_code = models.CharField('Gearbox Code', max_length=100, blank=True, help_text='Input Gearbox code')
    color = models.CharField('Color', max_length=20, help_text='Input Color Code example(LC5J)')

    BODY_CHOOSE = (
        ('cabriolet', 'Cabriolet'),
        ('coupe', 'Coupe'),
        ('sedan', 'Sedan'),
        ('station', 'Station'),
        ('hatchback', 'Hatchback'),
        ('Unknown', 'Unknown')
    )

    body_type = models.CharField(
        max_length=20,
        choices=BODY_CHOOSE,
        blank=True,
        default="Unknown",
        help_text='Choose body type',
    )
    parts = models.ManyToManyField('Part', blank=True, related_name='cars', help_text='Link parts to this car')

    def __str__(self):
        return f'{self.car_model.brand} {self.car_model.model} {self.years}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.car_cover.path)
        if img.height > 225 or img.width > 400:
            output_size = (400, 225)
            img.thumbnail(output_size)
            img.save(self.car_cover.path)


class Part(models.Model):
    AVAILABLE_CHOOSE = (
        ('Available', 'Available'),
        ('Sold', 'Sold')
    )
    status = models.CharField(
        max_length=20,
        choices=AVAILABLE_CHOOSE,
        blank=True,
        default='Available',
        help_text='Choose part status'
    )
    part_oem = models.CharField('Part OEM', max_length=100, help_text='Input OEM Code example(A1237300705)')
    part_name = models.CharField('Part name', max_length=100, null=True,
                                 help_text='Write part name example(Audi front-driver doors)')
    part_picture = models.ImageField('Cover', default="part_pics/no-image.jpg", upload_to='covers', null=True)
    part_picture_2 = models.ImageField('Cover2', default="part_pics/no-image.jpg", upload_to='covers', null=True,
                                       )
    part_picture_3 = models.ImageField('Cover3', default="part_pics/no-image.jpg", upload_to='covers', null=True,
                                       )
    part_picture_4 = models.ImageField('Cover4', default="part_pics/no-image.jpg", upload_to='covers', null=True,
                                       )
    part_description = models.CharField('Part description', null=True, max_length=250,
                                        help_text='Write part description')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    CONDITION_CHOOSE = (
        ('new', 'NEW'),
        ('used', 'USED'),
        ('damaged', 'DAMAGED')
    )
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOOSE,
        blank=True,
        help_text='Choose condition part',
    )

    SIDE_CHOOSE = (
        ('left', 'Left'),
        ('right', 'Right'),
        ('rear-left', 'Rear-Left'),
        ('rear-right', 'Rear-Right')
    )
    side = models.CharField(
        max_length=20,
        choices=SIDE_CHOOSE,
        blank=True,
        help_text='Choose part side',
    )
    part_type = models.ForeignKey('PartType', on_delete=models.CASCADE, null=False,
                                  help_text='Choose part type')
    price = models.FloatField('Price', help_text='Input part price example(199.99)')

    def __str__(self):
        return f'{self.part_oem}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.part_picture.path)
        if img.height > 225 or img.width > 300:
            output_size = (300, 225)
            img.thumbnail(output_size)
            img.save(self.part_picture.path)


class PartType(models.Model):
    PART_TYPE = (
        ('air_condition', 'Air conditioning-heating system/radiators'),
        ('body_parts', 'Body parts'),
        ('brake_system', 'Brake system'),
        ('electronic_system', 'Electronic system'),
        ('door', 'Door'),
        ('engine', 'Engine'),
        ('front_body', 'Front body parts'),
        ('rear_body', 'Rear body parts'),
        ('front_axle', 'Front axle'),
        ('rear_axle', 'Rear axle'),
        ('fuel_system', 'Fuel mixture system'),
        ('exhaust_system', 'Gas exhaust system'),
        ('gearbox', 'Gearbox/clutch/transmission'),
        ('glass', 'Glass'),
        ('headlight_system', 'Headlight washing/cleaning system'),
        ('lighting_system', 'Lighting system'),
        ('other_parts', 'Other parts'),
        ('wheels', 'Wheels/tires/caps')
    )
    part_type = models.CharField(
        max_length=100,
        choices=PART_TYPE,
        blank=True,
        null=True,
        help_text='Choose part type',
    )

    def __str__(self):
        return f'{self.part_type}'


class ToDoList(models.Model):
    PROGRESS_TYPE = (
        ('new', 'New'),
        ('working', 'Working'),
        ('stuck', 'Stuck'),
        ('pause', 'Pause'),
        ('almost done', 'Almost Done'),
        ('done', 'Done')
    )
    list_progress = models.CharField(
        max_length=100,
        choices=PROGRESS_TYPE,
        blank=True,
        null=True,
        default='new',
        help_text='Progressive',
    )

    name = models.CharField('Name', null=True, max_length=100, help_text='Input name progress')
    comment = models.CharField('Comment', null=True, max_length=100, help_text='Input comment')

    def __str__(self):
        return f'{self.list_progress}'

    class Meta:
        ordering = ['id']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    STATUS_CHOOSE = (
        ('Not verified', 'Not verified'),
        ('Verified', 'Verified')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOOSE,
        blank=True,
        default='Not verified',
        help_text='Choose profile status'
    )
    cover = models.ImageField(default="profile_pics/no-image.jpg", null=True, upload_to="profile_pics")
    city = models.CharField('City', max_length=100, null=True, blank=True, help_text='Input city name example(Vilnius)')
    address = models.CharField('Address', max_length=100, null=True, blank=True,
                               help_text='Input address example(Verkiu g. 2)')
    phone_number = models.CharField('Phone number', max_length=100, null=True, blank=True,
                                    help_text='Input phone number example(+37062222222)')

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.cover.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover.path)


class CartItem(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.part.part_oem}'
