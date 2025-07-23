from django import forms
from .models import Shipping_address

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping_address
        fields = ['full_name','shipping_mobile','shipping_address','shipping_city','shipping_pin','shipping_country']
        exclude = ['user']

    def __init__(self,*args,**kwargs):
        super(ShippingForm,self).__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})       
