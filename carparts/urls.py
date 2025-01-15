from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_id>', views.car, name='car'),
    path('parts/', views.parts, name='parts'),
    path('parts/<int:part_id>', views.part, name='part'),
    path('search/', views.search, name='search'),
    path('new_base/', views.new_base, name='new_base'),
    path('profile/', views.profile_main, name='profile_main'),
    path('profile-edit/', views.profile, name='profile'),
    path('myparts/', views.LoanedPartsByUserListView.as_view(), name='my-parts'),
    path('myparts/new', views.PartByUserCreateView.as_view(), name='my-parts-new'),
    path('myparts/update/<int:pk>', views.PartByUserUpdateView.as_view(), name='my-parts-update'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:part_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('profile_verification/', views.profile_verification, name='profile-verification'),
    path('mycars/', views.LoanedCarsByUserListView.as_view(), name='my-cars'),
    path('mycars/new', views.CarByUserCreateView.as_view(), name='my-cars-new'),
    path('mycars/update/<int:pk>', views.CarByUserUpdateView.as_view(), name='my-cars-update'),
]
