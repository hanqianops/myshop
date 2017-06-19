from .cart import Cart

def cart(request):
    """
    上下文处理器,可以在任何模板中使用该上下文内容
    """
    return {'cart': Cart(request)}