from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    """
    列出所有产品或者是筛选后的产品
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)  # 检索出可用产品
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)  # 指定类型的产品

    return render(request, "shop/product/list.html", locals())

def producr_detail(request, id, slug):
    """
    检索和展示单一的产品
    """

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    return render(request, "shop/product/detail.html", locals())

# from orders.tasks import add
# def test(r):
#     f = add.delay(22,33)
#     print(f.id)
#     return render(r,"test.html", locals())