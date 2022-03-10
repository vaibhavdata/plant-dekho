from logging import PlaceHolder
from django import forms
from nursery_ecommerce_app.models.product import Product,ProductGallery
from nursery_ecommerce_app.models.category import Category

class ProductForm(forms.ModelForm):
    #assignedDoctorId=forms.ModelChoiceField(queryset=Product.objects.all().filter(is_available=True),empty_label="value select", to_field_name="label")
    class Meta:
        model = Product
        fields = ('product_name','slug','stock','description','images','price','category','label',)
        
        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            self.fields['category'].queryset = Category.objects.all()
            self.fields['label'].queryset = Product.objects.all()
            
            for field in self.fields:
                self.fields[field].widget.attrs['class'] ="form-control"
        

