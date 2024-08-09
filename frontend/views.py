import random

from django.contrib.auth.models import User
from services.models import Service, ServiceImage
from users.models import Client, Artisan, Sector, ArtisanMediaLink, SubscriptionPlan
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from frontend.forms.user_info_form import UserInfoForm
from frontend.forms.activity_info_form import ActivityInfoForm
from frontend.forms.create_service_form import ServiceForm
from .models import HomeCarouselImage


# Create your views here.

def index(request):
    sectors = Sector.objects.all()
    home_images = HomeCarouselImage.objects.all()
    services = Service.objects.all()
    print(services)
    return render(request, 'index.html', {'sectors': sectors, 'home_image': home_images, 'services': services})


def pricing(request):
    subscription_plans = SubscriptionPlan.objects.all()
    response = {
        'plan0': subscription_plans[0],
        'plan1': subscription_plans[1],
        'plan2': subscription_plans[2],
    }
    return render(request, 'pages-pricing-tables.html', response)


@login_required
def update_profile(request):
    user = request.user
    artisan = Artisan.objects.get(user=user)
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            artisan.phone_number = form.cleaned_data['phone_number']
            artisan.sex = form.cleaned_data['sex']
            # artisan.birth_date = form.cleaned_data['birth_date']
            artisan.save()
            return redirect('user_profile')
        else:
            print("Form is not valid")
            print(form.errors)
            return redirect('user_profile')
    else:
        sectors = []
        for sector in Sector.objects.all():
            sectors.append((sector.id, sector.name))

        default_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone_number': artisan.phone_number,
            'sex': artisan.sex,
            'bio': artisan.bio,
            'whatsApp_phone': artisan.whatsApp_phone,
            'sectors': sectors,
        }

        form = UserInfoForm(default_data)
        activity_form = ActivityInfoForm()

        return render(request, 'dashboard/user-profile.html', {"form": form, "activity_form": activity_form})


def dashboard(request):
    return render(request, 'dashboard/index.html')


def dashboard_messages(request):
    pass


def dashboard_services(request):
    # services = Service.objects.filter(status= "active")
    services = Service.objects.all()
    return render(request, 'dashboard/sevice-list.html', {'services': services})


def dashboard_service_detail(request):
    pass


def create_service(request):
    pass


def delete_service(request):
    pass


def edit_service(request):
    pass


@login_required
def edit_profile(request):
    template_name = "dashboard/my-profile.html"
    # if request.method == 'POST':
    #     form = ArtisanForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('artisan_detail', pk=form.instance.pk)  # Rediriger vers la vue de détail de l'artisan
    # else:
    #     sectors_choices = [(sector.pk, sector.name) for sector in Sector.objects.all()]
    #     form = ArtisanForm()
    # print(sectors_choices)
    # form.fields['sectors'].choices = sectors_choices
    # sectors = Sector.objects.filter(is_delete=False)
    # user = request.user
    # artisan = Artisan.objects.get(user=user)
    # response = {'sectors': sectors, "artisan": artisan}
    # if request.method == 'POST':
    #     profile_image = None
    #     error_message = None
    #     form_is_valid = True
    #     try:
    #         profile_image = request.FILES['image_profile']
    #     except MultiValueDictKeyError:
    #         print("Error to get profile image")
    #     sectors = request.POST.getlist('sectors')
    #     first_name = request.POST.get('first_name', "")
    #     last_name = request.POST.get('last_name', "")
    #     phone = request.POST.get('phone', None)
    #     whatsapp = request.POST.get('whats_app_phone', "")
    #     email = request.POST.get('email', None)
    #     bio = request.POST.get('bio', None)
    #     sex = request.POST.get('sex', None)
    #     city = request.POST.get('city', None)
    #     twitter = request.POST.get('twitter', None)
    #     facebook = request.POST.get('facebook_link', None)
    #     instagram = request.POST.get('instagram_link', None)
    #     titok = request.POST.get('titok_link', None)
    #     youtube = request.POST.get('youtube_link', None)
    #
    #     if profile_image is None:
    #         error_message = "\nVous devez ajouter votre photo"
    #         form_is_valid = False
    #
    #     if sectors is None:
    #         error_message = "\nVous devez sélectionner au moins un secteur d'activité"
    #         form_is_valid = False
    #
    #     if phone is None:
    #         error_message = "\nVous devez ajouter votre numéro de télephone"
    #         form_is_valid = False
    #
    #     if email is None:
    #         error_message = "\nVous devez ajouter votre email"
    #         form_is_valid = False
    #
    #     if bio is None:
    #         error_message = "\nVous devez ajouter votre bio (une petite description de vous ou votre activité)"
    #         form_is_valid = False
    #
    #     if sex is None:
    #         error_message = "\nVous devez sélectionner votre sex"
    #         form_is_valid = False
    #     if city is None:
    #         error_message = "\nVous devez ajouter votre ville"
    #         form_is_valid = False
    #     if form_is_valid:
    #         user.first_name = first_name
    #         user.last_name = last_name
    #         user.email = email
    #         user.save()
    #         sector_list = []
    #         for sector in sectors:
    #             sct = Sector.objects.get(pk=sector)
    #             sector_list.append(sct)
    #         if len(sector_list) > 0:
    #             artisan.sectors = sector_list
    #         artisan.bio = bio
    #         artisan.phone_number = phone
    #         artisan.whatsapp = whatsapp
    #         artisan.city = city
    #         artisan.sex = sex
    #         artisan.profile_image = profile_image
    #
    #         if facebook is not None:
    #             ArtisanMediaLink.objects.create(artisan=artisan, media_type="fk", url=facebook)
    #         if titok is not None:
    #             ArtisanMediaLink.objects.create(artisan=artisan, media_type="tk", url=titok)
    #         if instagram is not None:
    #             ArtisanMediaLink.objects.create(artisan=artisan, media_type="int", url=titok)
    #         if twitter is not None:
    #             ArtisanMediaLink.objects.create(artisan=artisan, media_type="tw", url=twitter)
    #         if youtube is not None:
    #             ArtisanMediaLink.objects.create(artisan=artisan, media_type="yt", url=youtube)
    #         artisan.save()
    #         response['success_message'] = "Vos données ont bien été enregistrer"
    #
    #     else:
    #         response['error_message'] = error_message

    return render(request, template_name, )


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'auth/login.html', {"message": "invalid username or password .."})
        else:
            return render(request, 'auth/login.html', {"message": "invalid username or password"})
    return render(request, 'auth/login.html')


def user_logout(request):
    logout(request)
    return redirect('index')


def register_artisan(request):
    subscription_name = request.GET.get('subscription_name')
    print(subscription_name)
    selected_subscription = SubscriptionPlan.objects.get(name=subscription_name)
    error_message = {}
    form = UserInfoForm()
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User.objects.create_user(username=cleaned_data['email'], first_name=cleaned_data['first_name'],
                                            last_name=cleaned_data['last_name'], )
            user.set_password(cleaned_data['password1'])
            user.save()
            login(request, user)
            artisan = Artisan.objects.create(user=user, subscription_plan=selected_subscription,
                                             phone_number=cleaned_data['phone_number'])
            artisan.phone_number = cleaned_data['phone_number']
            artisan.sex = cleaned_data['sex']
            artisan.save()
            return redirect('register_artisan_step_2')
        else:
            print("Form is not valid")
            print(form.errors)
            error_message['form'] = form.errors

    return render(request, 'auth/register-artisan/register-artisan.html',
                  {'form': form, 'selected_subscription': selected_subscription, 'error_message': error_message})


def save_activity_info(request):
    sectors = Sector.objects.all()

    form = ActivityInfoForm()
    sector_choice = [(sector.id, sector.name) for sector in sectors]
    error_message = {}
    if request.method == 'POST':
        form = ActivityInfoForm(request.POST, request.FILES)
        selected_sector_id = request.POST.get('sector')
        if form.is_valid() and selected_sector_id is not None:
            cleaned_data = form.cleaned_data
            artisan = Artisan.objects.get(user=request.user)
            selected_sector = Sector.objects.get(id=selected_sector_id)
            artisan.sector = selected_sector
            artisan.profile_image = cleaned_data['profile_image']
            artisan.whatsApp_phone = cleaned_data['whatsApp_phone']
            artisan.bio = cleaned_data['bio']
            artisan.save()
            return redirect('register_artisan_step_3')
        else:
            print("Form is not valid")
            print(form.errors)
            print()
            error_message['form'] = form.errors

    return render(request, 'auth/register-artisan/step-2-activity-info.html',
                  {'form': form, 'sectors': sectors, 'error_message': error_message})


mock_location = locations = [
    {
        'city': 'Abidjan',
        'town': 'Plateau',
        'address': 'Avenue Chardy',
        'location_lat': '5.322139',
        'location_lon': '-4.007913'
    },
    {
        'city': 'Abidjan',
        'town': 'Cocody',
        'address': 'Université Félix Houphouët-Boigny',
        'location_lat': '5.341248',
        'location_lon': '-4.007215'
    },
    {
        'city': 'Abidjan',
        'town': 'Yopougon',
        'address': 'Marché de Yopougon',
        'location_lat': '5.354781',
        'location_lon': '-4.026229'
    },
    {
        'city': 'Abidjan',
        'town': 'Treichville',
        'address': 'Boulevard de Marseille',
        'location_lat': '5.308299',
        'location_lon': '-4.015655'
    },
    {
        'city': 'Abidjan',
        'town': 'Adjamé',
        'address': 'Place Adjamé',
        'location_lat': '5.374489',
        'location_lon': '-4.014254'
    },
    {
        'city': 'Abidjan',
        'town': 'Koumassi',
        'address': 'Centre Commercial Koumassi',
        'location_lat': '5.332762',
        'location_lon': '-4.046678'
    },
    {
        'city': 'Abidjan',
        'town': 'Abobo',
        'address': 'Marché d’Abobo',
        'location_lat': '5.402267',
        'location_lon': '-4.056923'
    },
    {
        'city': 'Abidjan',
        'town': 'Bingerville',
        'address': 'Centre-ville de Bingerville',
        'location_lat': '5.429287',
        'location_lon': '-3.974183'
    },
    {
        'city': 'Abidjan',
        'town': 'Riviera',
        'address': 'Riviera Palmeraie',
        'location_lat': '5.367369',
        'location_lon': '-4.035048'
    },
    {
        'city': 'Abidjan',
        'town': 'Marcory',
        'address': 'Avenue des Martyrs',
        'location_lat': '5.314646',
        'location_lon': '-4.010106'
    }
]


def save_activity_location(request):
    error_message = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        town = request.POST.get('town')
        address = request.POST.get('address')
        if city and town and address:
            artisan = Artisan.objects.get(user=request.user)
            artisan.city = city
            artisan.town = town
            artisan.address = address
            location = mock_location[random.randint(0, len(mock_location) - 1)]
            artisan.location_lat = location['location_lat']
            artisan.location_lon = location['location_lon']
            artisan.save()
            return redirect('index')
        else:
            error_message['form'] = "Merci de vérifier les informations"

    return render(request, 'auth/register-artisan/step-3-location.html')


def register(request):
    if request.method == 'POST':

        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password_confirm = request.POST.get('confirm_password', None)
        is_artisan = request.POST.get('is_artisan', None)
        if username and email and password and password_confirm and is_artisan:
            if password == password_confirm:
                if User.objects.filter(username=username).exists():
                    return render(request, 'auth/register.html', {"message": "Username already taken"})
                else:
                    user = User.objects.create_user(username, email, password)
                    user.save()

                    if is_artisan:
                        artisan = Artisan(user=user)
                        artisan.save()
                    else:
                        client = Client(user=user)
                        client.save()

                    login(request, user)

                    return redirect('index')
            else:
                return render(request, 'auth/register.html', {"message": "Passwords must match"})
        else:
            return render(request, 'auth/register.html', {"message": "Username and password fields are required"})

    return render(request, 'auth/register.html')


@login_required(login_url='pricing')
def create_service(request):
    data = {
        "main_image": "services/peinture_interieure.jpg",
        "name": "Peinture intérieure",
        "description": "Travaux de peinture pour tous types de surfaces intérieures, avec une large gamme de couleurs.",
        "price": 5000.00,
        "price_type": "Par mètre carré",
        "city": "Abidjan",
        "town": "Treichville",
        "address": "Avenue 14"
    }
    form = ServiceForm(data)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        auther_image = request.FILES.getlist('auther_images')
        location = mock_location[random.randint(0, len(mock_location) - 1)]
        if form.is_valid() and auther_image:
            clear_data = form.cleaned_data
            main_image = clear_data['main_image']
            artisan = Artisan.objects.get(user=request.user)
            sector = artisan.sector

            service = Service.objects.create(
                artisan=artisan,
                sector=sector,
                main_image=main_image,
                name=clear_data['name'],
                description=clear_data['description'],
                price=clear_data['price'],
                price_type=clear_data['price_type'],
                address=clear_data['address'],
                city=clear_data['city'],
                town=clear_data['town'],
                location_lat= location["location_lat"],
                location_lon= location["location_lon"],
                status="waiting"
            )
            service.save()
            print("Save Service")
            for image in auther_image:
                save_image = ServiceImage.objects.create(service=service, image=image)
                save_image.save()
            return redirect('dashboard')
        else:
            print("Form is not valid")
            print(auther_image)
            print(form.errors)
            print(request.FILES)
            print(request.POST)

    return render(request, 'dashboard/add-service.html', {'form': form})
