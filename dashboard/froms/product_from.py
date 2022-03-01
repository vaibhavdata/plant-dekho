from django import forms
from nursery_ecommerce_app.models.product import Product,ProductGallery
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','slug','description','price','images','stock','label','category')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] ="form-control"