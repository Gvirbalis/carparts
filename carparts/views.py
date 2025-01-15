from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import User
from django.views.generic import UpdateView

from .forms import UserUpdateForm, ProfileUpdateForm, UserCarCreateForm, UserPartCreateForm
from .models import Car, Part, CartItem


# Create your views here.
def index(request):
    cars_count = Car.objects.all().count()
    parts_count = Part.objects.all().count()
    context = {
        'cars_count': cars_count,
        'parts_count': parts_count,
    }
    return render(request, 'index.html', context=context)


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not username:
            messages.error(request, 'Username cannot be empty!')
            return redirect('register')

        if not email:
            messages.error(request, 'Email cannot be empty!')
            return redirect('register')

        if password == password2:
            if len(password) < 8:
                messages.error(request, 'Password must be at least 8 characters long!')
                return redirect('register')

            # Ensure password is not just digits
            if password.isdigit():
                messages.error(request, 'Password cannot be only digits!')
                return redirect('register')

            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username already {username} exits!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with email {email} already exits!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} successfully registered!')
                    return redirect('login')
        else:
            messages.error(request, 'Password not mach!')
            return redirect('register')
    return render(request, 'register.html')


def cars(request):
    paginator = Paginator(Car.objects.all().order_by('id'), 2)
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)
    cars_count = Car.objects.all().count()
    context = {
        'cars': cars,
        'cars_count': cars_count
    }
    return render(request, 'cars.html', context=context)


def car(request, car_id):
    single_car = get_object_or_404(Car, pk=car_id)
    return render(request, 'car.html', {'car': single_car})


def parts(request):
    paginator = Paginator(Part.objects.filter(status__exact='Available').order_by('id'), 5)
    page_number = request.GET.get('page')
    parts = paginator.get_page(page_number)
    parts_count = Part.objects.filter(status__exact='Available').count()
    context = {
        'parts': parts,
        'parts_count': parts_count
    }
    return render(request, 'parts.html', context=context)


def part(request, part_id):
    single_part = get_object_or_404(Part, pk=part_id)
    associated_cars = Car.objects.filter(parts=single_part)
    context = {
        'part': single_part,
        'cars': associated_cars,
    }
    return render(request, 'part.html', context=context)


def search(request):
    query = request.GET.get('query')
    search_results = Part.objects.filter(Q(part_oem__icontains=query)
                                         | Q(part_name__icontains=query) | Q(part_description__icontains=query))
    return render(request, 'search.html', {'parts': search_results, 'query': query})


def new_base(request):
    cars_count = Car.objects.all().count()
    parts_count = Part.objects.all().count()
    context = {
        'cars_count': cars_count,
        'parts_count': parts_count,
    }
    return render(request, 'new_base.html', context=context)


@login_required
def profile_main(request):
    return render(request, 'profile_main.html')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)


class LoanedPartsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Part
    template_name = 'user_parts.html'
    paginate_by = 2

    def get_queryset(self):
        return Part.objects.filter(owner=self.request.user).order_by('status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts_count'] = Part.objects.filter(owner=self.request.user, status__exact='Available').count()
        return context


class PartByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Part
    success_url = "/carparts/myparts/"
    template_name = 'user_part_form.html'
    form_class = UserPartCreateForm

    def form_valid(self, form):
        if self.request.user.profile.status == 'Verified':
            form.instance.owner = self.request.user
            return super().form_valid(form)
        else:
            return redirect('profile-verification')


class PartByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Part
    success_url = "/carparts/myparts/"
    template_name = 'user_part_form.html'
    form_class = UserPartCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        part = self.get_object()
        return self.request.user == part.owner


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.part.price for item in cart_items if item.part.status == 'Available')
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def add_to_cart(request, part_id):
    product = Part.objects.get(id=part_id)
    cart_item, created = CartItem.objects.get_or_create(part=product,
                                                        user=request.user)
    cart_item.save()
    return redirect('view_cart')


@login_required
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


def profile_verification(request):
    return render(request, 'profile-verification.html')


class LoanedCarsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = 'user_cars.html'
    paginate_by = 2

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars_count'] = Car.objects.filter(owner=self.request.user).count()
        return context


class CarByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    success_url = "/carparts/mycars/"
    template_name = 'user_car_form.html'
    form_class = UserCarCreateForm

    def form_valid(self, form):
        if self.request.user.profile.status == 'Verified':
            form.instance.owner = self.request.user
            return super().form_valid(form)
        else:
            return redirect('profile-verification')


class CarByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    success_url = "/carparts/mycars/"
    template_name = 'user_car_form.html'
    form_class = UserCarCreateForm

    def get_form(self, **kwargs):
        form = super().get_form()
        form.fields['parts'].queryset = Part.objects.filter(owner=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner
