from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from  cart.cart import Cart
from .forms import OrderCreateForm
from .models import Order
from .models import OrderItem
from .tasks import order_created
from django.views.generic import View


@staff_member_required  # 检查用户请求这个页面的is_active以及is_staff字段是被设置为True
def admin_order_detail(request, order_id):
    """
    扩展管理站点,定制一个订单详情页面
    """
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order/detail.html', locals())

class OrderCreate(View):

    def post(self,request):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()  # 清楚购物车
            order_created.delay(order.id)  # 调用异步任务,发送邮件
            return render(request, 'orders/order/created.html', locals())

    def get(self, request):
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', locals())
