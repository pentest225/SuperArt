from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Service, Message, ServiceRating, RatingImage
from django.db.models import Q
from users.models import Sector
from .forms import MessageForm
from django.contrib.auth.decorators import login_required


def products(request):
    sector_name = request.GET.get('sector_name')
    service_name = request.GET.get('service_name')
    address = request.GET.get('address')
    location_lat = request.GET.get('location_lat')
    location_lon = request.GET.get('location_lon')
    tags = request.GET.getlist('tags')

    sectors = Sector.objects.filter(is_delete=False)
    services = Service.objects.filter(is_delete=False, status='active')

    if sector_name and sector_name != 'all':
        services = services.filter(sector__name__icontains=sector_name)

    if service_name:
        services = services.filter(name__icontains=service_name)

    if address:
        services = services.filter(
            Q(city__icontains=address) | Q(town__icontains=address) | Q(address__icontains=address))

    if location_lat and location_lon:
        services = services.filter(location_lat=location_lat, location_lon=location_lon)

    if tags:
        services = services.filter(tags__name__in=tags).distinct()
    print("Patrick Services", services)
    response = {
        'services': services,
        'sectors': sectors,
        'service_name': service_name,
        'address': address,
        'sector_name': sector_name
    }

    return render(request, 'product/products-list.html', response)


def product(request, pk):
    service = Service.objects.get(pk=pk)
    data = {
        'chanel': 'message',
        'page_redirect': f'/annonces/' + str(service.id) + '/',
        'receiver_id': str(service.artisan.user.id),
        'content': "Bonjour j'ai besoin d'un menuisier pour changer la configuration de mon lit qui prend trop palce dans le VASTE studios de cocody ;)  "
    }
    message = MessageForm(data)

    result = {'service': service, 'message_form': message, 'add_review_success': None}
    if request.method == 'POST':
        loader_images = request.FILES.getlist('images')
        service_rating = request.POST.get('rating', '0')
        quality_rating = request.POST.get('quality', '0')
        client = request.user
        print(request.POST)
        print(service_rating)
        print(quality_rating)
        content = request.POST.get('content')
        rating = int(service_rating) + int(quality_rating) / 2
        new_rating = ServiceRating.objects.create(
            client=client,
            service=service,
            rating=rating,
            value_for_money=quality_rating,
            service_rating=service_rating,
            message=content
        )
        new_rating.save()
        for image in loader_images:
            rating_image = RatingImage.objects.create(rating=new_rating, image=image)
            rating_image.save()
        result['add_review_success'] = "Votre avis a bien été enregistré"

    return render(request, template_name='product/product-detail.html', context=result)


@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            sender = request.user
            print(cleaned_data)
            receiver = User.objects.get(id=cleaned_data['receiver_id'])
            new_message = (Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=cleaned_data['content'],
                chanel=cleaned_data['chanel'])
            )
            new_message.save()
            return redirect(cleaned_data['page_redirect'])
        else:
            return redirect('services:products-list')
    else:
        return redirect('index')
