from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# 验证器是一个可调用的对象，它接受一个值，并在不符合一些规则时抛出ValidationError异常。验证器有助于在不同类型的字段之间重复使用验证逻辑。

class Coupon(models.Model):
    """
    存储优惠券
    """
    code = models.CharField(max_length=50, unique=True)  # 用户必须要输入的代码来将优惠券应用到他们购买的商品中
    valid_from = models.DateTimeField()  # 优惠券生效的时间
    valid_to = models.DateTimeField()  # 优惠券会在过期时间
    discount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])    # 使用验证器来限制接收的最小值和最大值
    active = models.BooleanField()  # 优惠券是否激活

    def __str__(self):
        return self.code




