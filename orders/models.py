from django.db import models
from shop.models import Product

# 当购物车已经结账完毕时，你需要把订单保存进数据库中。订单将要保存客户信息和他们购买的产品信息。
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)  # 区分支付和未支付订单

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        """
        得到订单中购买物品的总花费
        """
        return  sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    """
    保存物品，数量和每个物品的支付价格
    """
    order = models.ForeignKey(Order, related_name="items")
    product = models.ForeignKey(Product, related_name="order_items")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        """
        返回物品的花费
        """
        return self.price * self.quantity
