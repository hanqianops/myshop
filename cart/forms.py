from django import forms
from django.forms import widgets

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 5)]

class CartAddProductForm(forms.Form):
    """
    为了把物品添加进购物车，我们需要一个允许用户选择数量的表单
    """
    quantity = forms.TypedChoiceField(
                choices=PRODUCT_QUANTITY_CHOICES,
                coerce=int,   # 把输入转换为整数
                # widget=widgets.Select(attrs={'class':'form-control'})
                )
    update = forms.BooleanField(required=False,
                initial=False,
                widget=forms.HiddenInput)