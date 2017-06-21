from django.shortcuts import render, redirect, get_object_or_404
from  django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST  # 只响应 POST 请求，因为这个视图将会变更数据
def cart_add(request, product_id):
    """
    向购物车添加新的产品或者更新当前产品的数量
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd["quantity"],
                 update_quantity=cd["update"])

    return redirect("cart:cart_detail")


def cart_remove(request, product_id):
    """
    接收产品 ID 作为参数,根据给定的产品 ID 检索相应的 Product 实例，
    然后将它从购物车中删除。
    然后，将用户重定向到 cart_detail URL
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return  redirect("cart:cart_detail")

def cart_detail(request):
    """
    购物车详情
    """
    cart = Cart(request)
    for item in cart:
        # 每一个购物车中的物品创建了 CartAddProductForm 实例来允许用户改变产品的数量。
        # 把表单和当前物品数量一同初始化，然后把 update 字段设为 True ，
        # 这样当提交表单到 cart_add 视图时，当前的数量就被新的数量替换了。
        item['update_quantity_form'] = CartAddProductForm(
                                    initial={'quantity': item['quantity'],
                                    'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})

