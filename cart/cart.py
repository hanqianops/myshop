from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    """
    可以让我们管理购物车。我们需要把购物车与一个 request 对象一同初始化
    """
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session  # 保存当前的会话

        # 从当前会话中获取购物车。如果当前会话中没有购物车，就在会话中设置一个空字典，
        # 这样就可以在会话中设置一个空的购物车。购物车字典使用产品 ID 作为键，
        # 以数量和价格为键值对的字典为值。这样做，就能保证一个产品在购物车当中不被重复添加；
        # 我们也能简化获取任意购物车物品数据的步骤。
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        向购物车当中添加产品或者更新产品的数量
        :param product:  需要在购物车中更新或者向购物车添加的 Product 对象
        :param quantity: 一个产品数量的可选参数。默认为 1
        :param update_quantity: 这是一个布尔值，它表示数量是否需要按照给定的数量参数更新（True），不然新的数量必须要被加进已存在的数量中（False）
        :return:
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        把购物车中所有的改动都保存到会话中
        然后用 session.modified = True 标记改动了的会话。这是为了告诉 Django 会话已经被改动，需要将它保存起来。
        """
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        从购物车字典中删除给定的产品
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        迭代购物车当中的物品，然后获取相应的 Product 实例
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        返回购物车中物品的总数量。
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        计算购物车中物品的总价
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        清空购物车会话
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True