from django.db.models.fields import DateTimeField
from django.shortcuts import render
from django.views import View
from .models import MenuItem, OrderModel, Category

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'customer/index.html')



class About(View):
    def get(self,request):
        return render(request, 'customer/about.html')



class Order(View):
    def get(self,request,*args,**kwargs):
        # get menu item
        pizza = MenuItem.objects.filter(category__name__contains='Pizza')
        sides = MenuItem.objects.filter(category__name__contains='Sides')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drinks')
        # pass into context
        context = {
            'pizzas':pizza,
            'sides':sides,
            'desserts':desserts,
            'drinks':drinks,
        }
        #render template
        return render(request, 'customer/order.html', context)


    def post(self,request,*args,**kwargs):
        # Get user details such as name, address etc
        print(request.POST.get('name'))

        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        is_delivery = request.POST.get('is_delivery')

        # Gets all the items the user has selected
        order_items = {
            'items' : []
        }

        selected_items = request.POST.getlist('items[]')
        selected_items.sort()

        print(selected_items)

        # each item is added into items list in the dictionary
        for item in selected_items:
            print(item)
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data ={
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items['items'].append(item_data)

        price = 0
        item_ids = []

        # Gets total price
        for item in order_items['items']:
            price = price + item['price']
            item_ids.append(item['id'])

        # if the checkbox is empty None is returned
        if is_delivery is None:
            is_delivery = False
        else:
            is_delivery = True

        # Creates an order object in the backend
        order = OrderModel.objects.create(price=price, name=name, email=email, address=address, postcode=postcode, is_delivery=is_delivery,)

        # Sends a confirmation email to the user
        print(email)
        send_email_to(email)

        order.items.add(*item_ids)


        context ={
            'items': order_items['items'],
            'total_price': price,
            }
        print(price)
        return render(request, 'customer/order_confirmation.html', context)




def send_email_to(email):
    subject = 'Order confirmation'
    message = 'Thanks for placing a Pizza Order Using My Website! Your Food will arrive shortly'
    from_email = 'setting.EMAIL_HOST'
    to_email = email

    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=False)
