from django.contrib import admin

# Register your models here.
from .models import Car, CarModel, Part, PartType, ToDoList, Profile, CartItem


class PartInline(admin.TabularInline):
    model = Car.parts.through
    extra = 0
    fk_name = 'car'
    can_delete = False


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'owner', 'car_model', 'years', 'fuel', 'engine', 'engine_code', 'power', 'gearbox', 'gearbox_code',
        'color',
        'body_type')
    list_filter = ('id', 'car_model', 'fuel')
    search_fields = ('car_model', 'years', 'engine')
    inlines = [PartInline]
    fieldsets = (
        ('Car', {'fields': ('car_model',)}),
        ('Car Info',
         {'fields': ('years', 'car_cover', 'color', 'body_type')}),
        ('Engine', {'fields': ('fuel', 'engine', 'engine_code', 'power')}),
        ('Gearbox', {'fields': ('gearbox_code', 'gearbox')}),
    )


class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'status', 'part_oem', 'condition', 'side', 'part_type', 'price')
    list_editable = ('status',)
    list_filter = ('part_oem', 'part_type', 'side')
    search_fields = ('part_oem',)


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'list_progress', 'name')
    list_editable = ('list_progress',)


admin.site.register(Profile)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(PartType)
admin.site.register(ToDoList, ToDoListAdmin)
admin.site.register(CartItem)
