"""
创建产品目录模型
    商店中的目录由不同分类的产品组成
    产品有以下字段：
        名字、描述（可选）、图片（可选）
"""
from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    产品分类模型
    """
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'category'

    def get_absolute_url(self):
        """
        get_absolute_url() 是检索一个对象的 URL 约定俗成的方法。
        定义Model的对象的查看地址,为每个请求对象生产URL
        object.get_absolute_url
        """
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    产品模型，一对多，一个产品只能属于一个分类，一个分类可以包含多个产品；
    name： 产品名字
    slug: 用来为这个产品建立URL的slug
    image: 产品图片
    description: 产品描述
    price: 产品价格，浮点数；这个字段使用 Python 的 decimal.Decimal 元类来保存一个固定精度的十进制数。max_digits 属性可用于设定数字的最大值， decimal_places 属性用于设置小数位数。
    stock: 产品库存
    acailable: 布尔值用于展示产品是否可供购买。这使得我们可在目录中使产品废弃或生效。
    created: 当对象被创建时这个字段被保存。
    update: 当对象被更新时这个字段被保存。
    """
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        使用 index_together 元选项来指定 id 和 slug 字段的共同索引。两个字段被索引在一起可以提高使用双字段查询的效率。
        """
        ordering = ('name',)
        index_together = (('id','slug'))

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

    def __str__(self):
        return self.name