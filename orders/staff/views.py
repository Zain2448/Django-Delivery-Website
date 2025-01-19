from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel, MenuItem, Category


# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'account/login.html')


class Overview(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):
        orders = OrderModel.objects.all()

        # loop through the order to get the total price
        today_revenue = 0
        today_orders = len(orders)
        for order in orders:
            today_revenue = today_revenue + order.price

        incomplete_orders = orders.filter(is_shipped=False)
        complete_orders = orders.filter(is_shipped=True)
        context = {
            'incomplete_orders': incomplete_orders,
            'complete_orders': complete_orders,
            'total_revenue': today_revenue,
            'total_orders': today_orders
        }
        return render(request, 'staff/order_overview.html', context)


    def test_func(self):
        # returns true if user is staff\
        return self.request.user.groups.filter(name='Staff').exists()



class OrderDetail(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self,request, my_id):
        order = OrderModel.objects.get(id=my_id)
        context = {
            'order': order,
        }
        return render(request, 'staff/order_details.html', context)

    def test_func(self):
        # returns true if user is staff\
        return self.request.user.groups.filter(name='Staff').exists()

    def post(self, request, my_id):
        order = OrderModel.objects.get(pk=my_id)
        order.is_shipped = True
        order.save()

        context = {
            'order': order
        }

        return render(request, 'staff/order_details.html', context)





class AddItem(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self,request):
        return render(request, 'staff/add_item.html')

    def test_func(self):
        # returns true if user is staff\
        return self.request.user.groups.filter(name='Staff').exists()

    def post(self,request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES['image']
        price = request.POST.get('price')
        category = request.POST.get('category')

        print(request.POST.get('name'))
        print(request.POST.get('description'))
        print(request.FILES['image'])
        print(request.POST.get('category'))
        print(request.POST.get('price'))
        item_id=MenuItem.objects.count()+1

        print(item_id)


        item = MenuItem.objects.create(id = item_id ,name=name, description=description, image=image, price=price,)
        word = Category.objects.get(id=2)
        print(word.name)
        item.category.add(Category.objects.all()[int(category)])



        return render(request, 'staff/add_item.html')
