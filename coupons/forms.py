from django import forms

class CouponApplyForm(forms.Form):
    """
    用户输入优惠券代码的表单
    """
    code = forms.CharField()


