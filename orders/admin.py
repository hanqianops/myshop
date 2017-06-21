import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse

from .models import Order, OrderItem


def export_to_csv(modeladmin, request, queryset):
    """
    导出csv文件
    """
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')  # 告诉浏览器，文档是个CSV文件不是HTML文件
    response['Content-Disposition'] = 'attachment;filename={}.csv'.format(opts.verbose_name)  # csv文件名
    writer = csv.writer(response)
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])  # 第一行是标题
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

from django.urls import reverse
def order_detail(obj):
    """
    订单详情
    """
    return '<a href="{}">订单详情</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id]))
order_detail.allow_tags = True   # 解释HTML标记

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated',order_detail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)